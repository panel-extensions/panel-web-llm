"""Command-line interface for launching the Panel WebLLM interface."""

import argparse

import panel as pn

from panel_web_llm.main import MODEL_MAPPING
from panel_web_llm.main import WebLLMInterface


def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Launch Panel WebLLM Interface")
    parser.add_argument(
        "--model",
        type=str,
        default="",
        help="Model slug to load (e.g., 'Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC'). If not provided, will default to the first option",
    )
    parser.add_argument(
        "--multiple-loads",
        action="store_true",
        help="Whether to allow loading different models multiple times",
        default=True,
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5006,
        help="The port to run the server on.",
    )
    parser.add_argument(
        "--address",
        type=str,
        default="0.0.0.0",
        help="The address to run the server on.",
    )
    return parser.parse_args()


def main():
    """Main function to launch the Panel app."""
    args = parse_args()

    if args.model:
        model_slug = args.model
    else:
        model_slug = sorted(value for models in MODEL_MAPPING.values() for sizes in models.values() for value in sizes.values())[0]

    interface = WebLLMInterface(
        model_slug=model_slug,
        multiple_loads=args.multiple_loads,
        load_on_init=True,
    )
    interface.servable()
    pn.serve(interface, port=args.port, address=args.address, show=True)


if __name__ == "__main__":
    main()
