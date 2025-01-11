# ✨ panel-web-llm

[![CI](https://img.shields.io/github/actions/workflow/status/panel-extensions/panel-web-llm/ci.yml?style=flat-square&branch=main)](https://github.com/panel-extensions/panel-web-llm/actions/workflows/ci.yml)
[![pypi-version](https://img.shields.io/pypi/v/panel-web-llm.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-web-llm)
[![python-version](https://img.shields.io/pypi/pyversions/panel-web-llm?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-web-llm)

This extension for HoloViz Panel introduces a client-side interface for running large language models (LLMs) directly in the browser.

It leverages WebLLM under the hood to provide an in-browser LLM execution environment, enabling fully client-side interactions without relying on server-side APIs.

## Features

- **Run LLMs in the Browser**: Execute large language models directly in the browser without requiring server-side APIs or cloud services.
- **Offline Capability**: Cache models locally in the browser, enabling offline use after initial download.
- **Model Variety**: Supports multiple models, including Llama 2 and Qwen 2.5. Check Available Models for the most up-to-date list.
- **Privacy-Preserving**: Keeps all computations client-side, ensuring data privacy and security.
- **Panel Integration**: Effortlessly incorporate LLM-powered features into interactive Panel applications.

## Pin Version

This project is **in its early stages**, so if you find a version that suits your needs, it’s recommended to **pin your version**, as updates may introduce changes.

## Installation

Install it via `pip`:

```bash
pip install panel-web-llm
```

## Usage

### Online

Try it out in [Examples](https://panel-extensions.github.io/panel-web-llm/examples/).

### Command Line Interface

Once installed, you may launch the web LLM in the terminal with the following command:

```bash
panel-web-llm
```

Once the server launches, the `Load <model_name>` button has been clicked, the model is cached in your browser.

That means, even if you **restart the server without internet, you can still run that same model offline**, as long as your browser cache is not cleared.

The following is an alias for convenience:

```bash
pllm
```

The default model used is `Qwen2.5-Coder-7B-Instruct-q4f16_1-MLC`. To default to another model:

```bash
panel-web-llm run <model_name>
```

Replace `<model_name>` with the name of the model you want to use. For a list of models:

```bash
panel-web-llm list
```

### Python

You can seamlessly integrate the Web LLM interface into your Panel applications:

```python
import panel as pn
from panel_web_llm import WebLLMInterface
pn.extension()

template = pn.template.FastListTemplate(
    title="Web LLM Interface", main=[WebLLMInterface()]
)
template.show()
```

If you don't like the built-in layout of `WebLLMInterface`, you can instead wrap `WebLLM` manually:

```python
import panel as pn
from panel_web_llm import WebLLM

pn.extension()

web_llm = WebLLM(load_layout="column")
chat_interface = pn.chat.ChatInterface(
    callback=web_llm.callback,
)

template = pn.template.FastListTemplate(
    title="Web LLM Interface",
    main=[chat_interface],
    sidebar=[web_llm.menu, web_llm],  # important to include `web_llm`
    sidebar_width=350,
)
template.show()
```

## Development

```bash
git clone https://github.com/panel-extensions/panel-web-llm
cd panel-web-llm
```

For a simple setup use [`uv`](https://docs.astral.sh/uv/):

```bash
uv venv
source .venv/bin/activate # on linux. Similar commands for windows and osx
uv pip install -e .[dev]
pre-commit run install
pytest tests
```

For the full Github Actions setup use [pixi](https://pixi.sh):

```bash
pixi run pre-commit-install
pixi run postinstall
pixi run test
```

This repository is based on [copier-template-panel-extension](https://github.com/panel-extensions/copier-template-panel-extension) (you can create your own Panel extension with it)!

To update to the latest template version run:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier update --defaults --trust
```

Note: `copier` will show `Conflict` for files with manual changes during an update. This is normal. As long as there are no merge conflict markers, all patches applied cleanly.

## ❤️ Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.
