# ✨ panel-web-llm

[![CI](https://img.shields.io/github/actions/workflow/status/panel-extensions/panel-web-llm/ci.yml?style=flat-square&branch=main)](https://github.com/panel-extensions/panel-web-llm/actions/workflows/ci.yml)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/panel-web-llm?logoColor=white&logo=conda-forge&style=flat-square)](https://prefix.dev/channels/conda-forge/packages/panel-web-llm)
[![pypi-version](https://img.shields.io/pypi/v/panel-web-llm.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-web-llm)
[![python-version](https://img.shields.io/pypi/pyversions/panel-web-llm?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-web-llm)
Extends HoloViz Panel with an interface that wraps a client-side LLM.

## Features

panel-web-llm

## Pin your version!

This project is **in its early stages**, so if you find a version that suits your needs, it’s recommended to **pin your version**, as updates may introduce changes.

## Installation

Install it via `pip`:

```bash
pip install panel-web-llm
```

## Usage

```python
import panel_web_llm
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

This repository is based on [copier-template-panel-extension](https://github.com/panel-extensions/copier-template-panel-extension).
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
