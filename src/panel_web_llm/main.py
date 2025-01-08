"""Main module."""

import asyncio

import panel as pn
import param
from panel.chat import ChatFeed
from panel.chat import ChatInterface
from panel.custom import JSComponent

from .settings import MODEL_MAPPING


class WebLLM(JSComponent):
    loaded = param.Boolean(
        default=False,
        doc="""
        Whether the model is loaded.""",
    )

    history = param.Integer(default=3)

    status = param.Dict(default={"text": "", "progress": 0})

    load_model = param.Event()

    model_slug = param.Selector()

    model_mapping = param.Dict(default=MODEL_MAPPING)

    running = param.Boolean(
        default=False,
        doc="""
        Whether the LLM is currently running.""",
    )

    temperature = param.Number(
        default=1,
        bounds=(0, 2),
        doc="""
        Temperature of the model completions.""",
    )

    _esm = """
    import * as webllm from "https://esm.run/@mlc-ai/web-llm";

    const engines = new Map()

    export async function render({ model }) {
      model.on("msg:custom", async (event) => {
        if (event.type === 'load') {
          if (!engines.has(model.model_slug)) {
            const initProgressCallback = (status) => {
              model.status = status
            }
            const mlc = await webllm.CreateMLCEngine(
               model.model_slug,
               {initProgressCallback}
            )
            engines.set(model.model_slug, mlc)
          }
          model.loaded = true
        } else if (event.type === 'completion') {
          const engine = engines.get(model.model_slug)
          if (engine == null) {
            model.send_msg({'finish_reason': 'error'})
          }
          const chunks = await engine.chat.completions.create({
            messages: event.messages,
            temperature: model.temperature ,
            stream: true,
          })
          model.running = true
          for await (const chunk of chunks) {
            if (!model.running) {
              break
            }
            model.send_msg(chunk.choices[0])
          }
        }
      })
    }
    """

    def __init__(self, **params):
        self._model_select = pn.widgets.NestedSelect(layout=pn.Row)
        self._load_button = pn.widgets.Button.from_param(
            self.param.load_model,
            disabled=self.param.loaded.rx().rx.or_(self.param.loading),
            align=("start", "end"),
        )
        self._model_select.param.watch(self._update_model_slug, "value")
        super().__init__(**params)
        if pn.state.location:
            pn.state.location.sync(self, {"model_slug": "model_slug"})
        self._buffer = []

    def _get_model_options(self, model_mapping):
        model_options = {
            model_name: {parameters: list(quantizations.keys()) for parameters, quantizations in model_mapping[model_name].items()}
            for model_name in sorted(model_mapping)
        }
        return model_options

    @param.depends("model_mapping", watch=True, on_init=True)
    def _update_model_select(self):
        self._model_select.param.update(
            options=self._get_model_options(self.model_mapping),
            levels=["Model", "Size", "Quantization"],
        )
        self.param["model_slug"].objects = sorted(value for models in MODEL_MAPPING.values() for sizes in models.values() for value in sizes.values())

    @param.depends("model_slug", watch=True)
    def _update_load_button(self):
        self._load_button.name = f"Load {self.model_slug}"

    def _update_model_slug(self, event):
        selected = self._model_select.value
        self.model_slug = self.model_mapping[selected["Model"]][selected["Size"]][selected["Quantization"]]

    def _load_model(self, event):
        self.loading = True
        self._send_msg({"type": "load"})

    @param.depends("loaded", watch=True)
    def _loaded(self):
        self.loading = False

    @param.depends("model_slug", watch=True)
    def _update_load_model(self):
        self.loaded = False

    def _handle_msg(self, msg):
        if self.running:
            self._buffer.insert(0, msg)

    async def create_completion(self, messages):
        self._send_msg({"type": "completion", "messages": messages})
        while True:
            await asyncio.sleep(0.01)
            if not self._buffer:
                continue
            choice = self._buffer.pop()
            yield choice
            reason = choice["finish_reason"]
            if reason == "error":
                raise RuntimeError("Model not loaded")
            elif reason:
                return

    def refresh_model_mapping(self):
        import re

        import bs4
        import requests

        text = requests.get("https://mlc.ai/models#mlc-models").text
        soup = bs4.BeautifulSoup(text, "html.parser")
        table = soup.find("table")
        links = table.find_all("a")
        model_mapping = {}
        for link in links:
            model_slug = link.get("href").rsplit("/", 1)[-1]
            model_label, model_quantization, _ = model_slug.rsplit("-", 2)
            model_parameters_re = re.search(r"\d+(\.\d+)?[Bbk]", model_label)
            try:
                model_parameters = model_parameters_re.group(0)
                model_name = model_label[: model_parameters_re.start()].rstrip("-").rstrip("_")
            except AttributeError:
                model_parameters = "-"
                model_name = model_label.rstrip("-").rstrip("_")
            if model_name not in model_mapping:
                model_mapping[model_name] = {}
            if model_parameters not in model_mapping[model_name]:
                model_mapping[model_name][model_parameters] = {}
            model_mapping[model_name][model_parameters][model_quantization] = model_slug
        self.model_mapping = model_mapping

    async def callback(self, contents: str, user: str, instance: ChatInterface):
        if not self.loaded:
            if self.loading:
                yield pn.pane.Markdown(f"## `{self.model_slug}`\n\n" + self.param.status.rx()["text"])
            else:
                yield {"user": "help", "object": "Please load the model first."}
            return
        self.running = False
        self._buffer.clear()

        messages = instance.serialize()
        message = ""
        async for chunk in self.create_completion(messages):
            message += chunk["delta"].get("content", "")
            yield message

    def menu(self):
        status = self.param.status.rx()
        model_config = pn.Row(
            self._model_select,
            pn.widgets.NumberInput.from_param(
                self.param.temperature,
            ),
            self._load_button,
            pn.indicators.Number(
                value=(status["progress"] * 100).rx.pipe(int),
                format="{value}%",
                font_size="25px",
                visible=self.param.loading,
                align=("start", "end"),
            ),
            pn.pane.Markdown(status["text"], visible=self.param.loading),
        )
        return pn.Card(
            model_config,
            margin=(5, 15),
            title="Model Settings",
        )


class WebLLMComponentMixin(param.Parameterized):
    def __init__(self, **params):
        super().__init__(**params)
        self.web_llm = WebLLM()
        self.callback = self.web_llm.callback
        self.help_text = "First load the model, then start chatting."
        self.header = self.web_llm.menu()


class WebLLMFeed(ChatFeed, WebLLMComponentMixin): ...


class WebLLMInterface(ChatInterface, WebLLMComponentMixin): ...
