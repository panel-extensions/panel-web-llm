"""Panel components for the WebLLM interface."""

import asyncio

import panel as pn
import param
from panel.chat import ChatFeed
from panel.chat import ChatInterface
from panel.custom import JSComponent

from .models import ModelParam
from .settings import MODEL_MAPPING


class WebLLM(JSComponent):
    """
    A Panel component for interacting with WebLLM models.

    This component provides an interface to load and interact with models served
    by the `web-llm` library. It manages model loading, chat completion,
    and provides controls for model selection and temperature.
    """

    history = param.Integer(
        default=10,
        bounds=(1, 100),
        doc="The number of previous messages to include in the completion.",
    )

    load_status = param.Dict(default={"text": "", "progress": 0})

    load_model = param.Event(doc="Event to trigger model loading.")

    load_layout = param.Selector(
        default="row",
        objects=["row", "column"],
        doc="""
        The layout type of the widgets.""",
    )

    model_slug = param.Selector(default="", doc="The model slug to load.")

    model_mapping = param.Dict(default=MODEL_MAPPING, doc="Nested mapping of model names to slugs.")

    multiple_loads = param.Boolean(
        default=True,
        doc="Whether to allow loading different models multiple times",
    )

    running = param.Boolean(
        default=False,
        doc="Whether the LLM is currently running.",
    )

    system = param.String(
        default="Be a world-class helper. Try to keep your answers concise.",
        doc="The system prompt for the model completion.",
    )

    temperature = param.Number(
        default=1,
        bounds=(0, 2),
        doc="The temperature for the model completion.",
    )

    loaded = param.Boolean(
        default=False,
        doc="Whether the model is loaded.",
    )

    loading = param.Boolean(
        default=False,
        doc="""
        Whether the model is currently loading.""",
    )

    refresh = param.Event(
        doc="""
        Click to load the latest available models from https://mlc.ai/models.
        Requires a network connection.
        """
    )

    _esm = """
        import * as webllm from "https://esm.run/@mlc-ai/web-llm";

        const engines = new Map()

        export async function render({ model }) {
        model.on("msg:custom", async (event) => {
            if (event.type === 'load') {
            model.loading = true
            if (!engines.has(model.model_slug)) {
                const initProgressCallback = (load_status) => {
                model.load_status = load_status
                }
                try {
                const mlc = await webllm.CreateMLCEngine(
                    model.model_slug,
                    { initProgressCallback }
                )
                engines.set(model.model_slug, mlc)
                model.loaded = true
                } catch (error) {
                model.load_status = {
                    progress: 0,
                    text: error.message + " Try again later, or try a different size/quantization.",
                };
                model.loaded = false;
                }
            }
            model.loading = false
            } else if (event.type === 'completion') {
            const engine = engines.get(model.model_slug)
            if (engine == null) {
                model.send_msg({ 'finish_reason': 'error' })
            }
            const chunks = await engine.chat.completions.create({
                messages: event.messages,
                temperature: model.temperature,
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
        """
        Initializes the WebLLM component.

        Args:
            **params:
                Keyword arguments for the Panel and Param base classes.
        """
        self._buffer = []
        load_layout = pn.Column if params.get("load_layout") == "column" else pn.Row
        self._model_select = pn.widgets.NestedSelect(layout=load_layout)
        self._model_select_placeholder = pn.pane.Placeholder(
            object=self._model_select,
        )
        super().__init__(**params)

        self._history_input = pn.widgets.IntSlider.from_param(
            self.param.history,
            disabled=self.param.loading,
            sizing_mode="stretch_width",
        )
        self._temperature_input = pn.widgets.FloatSlider.from_param(
            self.param.temperature,
            disabled=self.param.loading,
            sizing_mode="stretch_width",
        )
        self._refresh_button = pn.widgets.ButtonIcon.from_param(
            self.param.refresh,
            name="",
            align="end",
            icon="refresh",
            active_icon="check",
            toggle_duration=1000,
            margin=(10, -5, 5, 0),
            size="28px",
        )
        self._load_button = pn.widgets.Button.from_param(
            self.param.load_model,
            name=param.rx("Load ") + self.param.model_slug,
            loading=self.param.loading,
            align=("start", "end"),
            button_type="primary",
            description=None,  # override default text
        )
        load_status = self.param.load_status.rx()
        self._submit_row = pn.Row(self._refresh_button, self._load_button, align="end")
        load_row = load_layout(
            self._model_select_placeholder,
            self._submit_row,
            sizing_mode="stretch_width",
            margin=0,
        )
        config_row = pn.Row(
            self._temperature_input,
            self._history_input,
            sizing_mode="stretch_width",
            margin=0,
        )
        system_input = pn.widgets.TextAreaInput.from_param(
            self.param.system,
            auto_grow=True,
            resizable="height",
            sizing_mode="stretch_width",
        )
        load_progress = pn.Column(
            pn.indicators.Progress(
                value=(load_status["progress"] * 100).rx.pipe(int),
                visible=self.param.loading,
                sizing_mode="stretch_width",
                margin=(5, 10, -10, 10),
                height=30,
            ),
            pn.pane.HTML(
                load_status["text"],
                visible=load_status.rx.len() > 0,
            ),
        )
        self._card_header = pn.pane.HTML("<b>Model Settings</b>")
        self._card = pn.Card(
            load_row,
            config_row,
            system_input,
            load_progress,
            header=self._card_header,
            sizing_mode="stretch_width",
            margin=(5, 20, 5, 0),
            align="center",
        )
        self._model_select.param.watch(self._update_model_slug, "value")
        if pn.state.location:
            pn.state.location.sync(self, {"model_slug": "model_slug"})

    def _get_model_options(self, model_mapping):
        """
        Generates the model options for the nested select widget.

        Args:
            model_mapping (dict):
                A dictionary mapping model names to parameters and quantizations.

        Returns
        -------
            dict: A dictionary representing the model options.
        """
        model_options = {
            model_name: {parameters: list(quantizations.keys()) for parameters, quantizations in model_mapping[model_name].items()}
            for model_name in sorted(model_mapping)
        }
        return model_options

    @param.depends("model_mapping", watch=True, on_init=True)
    def _update_model_select(self):
        """Updates the model selection widget when the model_mapping changes."""
        options = self._get_model_options(self.model_mapping)
        levels = [
            {"name": "Model", "sizing_mode": "stretch_width"},
            {"name": "Size", "sizing_mode": "stretch_width"},
            {"name": "Quantization", "sizing_mode": "stretch_width"},
        ]
        value = None
        if self.model_slug:
            model_params = ModelParam.from_model_slug(self.model_slug)
            value = model_params.to_dict(levels)
        # TODO: Bug https://github.com/holoviz/panel/issues/7647
        # self._model_select.param.update(
        #     options=options,
        #     levels=levels,
        #     value=value,
        # )
        self._model_select = pn.widgets.NestedSelect(
            options=options,
            levels=levels,
            value=value,
            layout=self._model_select.layout,
        )
        self._model_select_placeholder.object = self._model_select
        self.param["model_slug"].objects = sorted(value for models in MODEL_MAPPING.values() for sizes in models.values() for value in sizes.values())

    def _update_model_slug(self, event):
        """
        Updates the model_slug parameter based on the selected model.

        Args:
            event (param.parameterized.Event):
                A change event from the model selection widget.
        """
        self.model_slug = ModelParam.from_nested_select(self._model_select).lookup_model_slug(self.model_mapping)

    @param.depends("model_slug", watch=True)
    def _update_nested_select(self):
        """Updates the nested select widget when the model slug changes."""
        model_param = ModelParam.from_model_slug(self.model_slug)
        self._model_select.value = model_param.to_dict(self._model_select.levels)

    @param.depends("load_model", watch=True)
    def _load_model(self):
        """Loads the model when the load_model event is triggered."""
        if self.model_slug in self._card_header.object:
            return
        self.load_status = {
            "progress": 0,
            "text": f"Preparing to load {self.model_slug}",
        }
        self._send_msg({"type": "load"})

    @param.depends("multiple_loads", watch=True)
    def _on_multiple_loads(self):
        if not self.multiple_loads and self.loaded:
            self._card.visible = False

    @param.depends("loading", watch=True)
    def _on_loading(self):
        self._model_select.disabled = self.loading

    @param.depends("loaded", watch=True)
    def _on_loaded(self):
        if self.loaded:
            self._card.collapsed = True
            if not self.multiple_loads:
                self._card.visible = False
            self._load_button.disabled = True
            self._card_header.object = f"Model Settings (Loaded: {self.model_slug})"
        else:
            self._card.visible = True
            self._load_button.disabled = False

    @param.depends("model_slug", watch=True)
    def _on_model_slug(self):
        self.loaded = False

    def _handle_msg(self, msg):
        """
        Handles messages from the WebLLM.

        Args:
            msg (dict):
                The message data received from the WebLLM.
        """
        if self.running:
            self._buffer.insert(0, msg)

    async def create_completion(self, messages):
        """
        Creates a chat completion with the WebLLM.

        Args:
            messages (list):
                A list of message dictionaries representing the chat history.

        Yields
        ------
             dict:  The response chunks from the LLM.

        Raises
        ------
            RuntimeError: If the model is not loaded.
        """
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

    @param.depends("refresh", watch=True)
    def refresh_model_mapping(self):
        """
        Refreshes the model mapping by fetching the latest from the mlc.ai website.

        This method scrapes the mlc.ai website to get the available models and their
        parameters.

        Requires bs4 and requests to be installed.
        """
        import bs4
        import requests  # type: ignore

        try:
            text = requests.get("https://mlc.ai/models#mlc-models").text
        except requests.ConnectionError:
            self._refresh_button.param.update(icon="wifi-off", active_icon="x", description="Connection unavailable.")
            return
        soup = bs4.BeautifulSoup(text, "html.parser")
        table = soup.find("table")
        links = table.find_all("a")
        model_mapping: dict = {}
        for link in links:
            model_slug = link.get("href").rsplit("/", 1)[-1]
            model_params = ModelParam.from_model_slug(model_slug)
            model_name = model_params.model
            model_parameters = model_params.size
            model_quantization = model_params.quantization
            if model_name not in model_mapping:
                model_mapping[model_name] = {}
            if model_parameters not in model_mapping[model_name]:
                model_mapping[model_name][model_parameters] = {}
            model_mapping[model_name][model_parameters][model_quantization] = model_slug
        self.model_mapping = model_mapping

    async def callback(self, contents: str, user: str, instance: ChatInterface):
        """
        Callback function for chat completion.

        Args:
            contents (str):
                The current user message.
            user (str):
                The username of the user sending the message.
            instance (ChatInterface):
                The ChatInterface instance.

        Yields
        ------
            dict or str: Yields either the messages as dict or a markdown string

        Raises
        ------
            RuntimeError: If the model is not loaded
        """
        if not self.loaded:
            return
        self.running = False
        self._buffer.clear()

        messages = [{"role": "system", "content": self.system}] + instance.serialize(limit=self.history)

        message = ""
        async for chunk in self.create_completion(messages):
            message += chunk["delta"].get("content", "")
            yield message

    @property
    def menu(self):
        """
        Returns the model selection widget.

        Returns
        -------
            pn.widgets.NestedSelect: The model selection widget.
        """
        return self._card


class WebLLMComponentMixin(param.Parameterized):
    """
    A mixin class for integrating the WebLLM component with other components.

    This mixin provides an easy way to add a WebLLM instance and its necessary
    attributes to other Panel components.
    """

    model_slug = param.String(
        doc="The model slug to load.",
    )

    multiple_loads = param.Boolean(
        default=True,
        doc="Whether to allow loading different models multiple times.",
    )

    load_on_init = param.Boolean(
        default=False,
        doc="Whether to load the model on initialization.",
    )

    web_llm_kwargs = param.Dict(default={}, doc="Keyword arguments to propagate to the WebLLM.")

    def __init__(self, **params):
        """
        Initializes the WebLLMComponentMixin.

        Args:
            **params:
                Keyword arguments for the Param base classes.
        """
        super().__init__(**params)
        self.web_llm = WebLLM(
            model_slug=self.model_slug,
            multiple_loads=self.multiple_loads,
            **self.web_llm_kwargs,
        )
        self.callback = self.web_llm.callback
        self.edit_callback = self._edit_callback
        self.header = pn.Column(self.web_llm.menu, self.web_llm)
        pn.state.onload(self._onload)

    def _edit_callback(self, contents, index, instance):
        instance.objects = instance.objects[: index + 1]
        self.respond()

    def _onload(self):
        if self.load_on_init:
            self.web_llm.load_model = True
        else:
            self.help_text = "Please first load the model, then start chatting."


class WebLLMFeed(ChatFeed, WebLLMComponentMixin):
    """See [ChatFeed](https://panel.holoviz.org/reference/chat/ChatFeed.html) for params and usage."""


class WebLLMInterface(ChatInterface, WebLLMComponentMixin):
    """See [ChatInterface](https://panel.holoviz.org/reference/chat/ChatInterface.html) for params and usage."""
