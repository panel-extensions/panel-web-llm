"""Command-line interface for launching the Panel WebLLM interface."""

import argparse
import sys

import panel as pn

from panel_web_llm.main import MODEL_MAPPING
from panel_web_llm.main import WebLLMInterface


def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Launch Panel WebLLM Interface")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Subparser for the 'list' command
    subparsers.add_parser("list", help="List all available models.")

    # Subparser for the 'run' command
    run_parser = subparsers.add_parser("run", help="Run the Panel WebLLM Interface.")
    run_parser.add_argument(
        "model_slug",  # positional argument for model_slug
        type=str,
        nargs="?",
        default="Qwen2.5-Coder-7B-Instruct-q4f16_1-MLC",
        help="Model slug to load",
    )
    run_parser.add_argument(
        "--multiple-loads",
        action="store_true",
        help="Whether to allow loading different models multiple times",
        default=True,
    )
    run_parser.add_argument(
        "--port",
        type=int,
        default=5006,
        help="The port to run the server on.",
    )

    # Preliminary parse to check if a command was provided.
    args, remaining = parser.parse_known_args()
    if args.command is None:
        # No command provided; default to 'run'
        sys.argv.insert(1, "run")
        args = parser.parse_args()
    return args


def main():
    """Main function to launch the Panel app."""
    args = parse_args()

    if args.command == "list":
        for model, sizes in MODEL_MAPPING.items():
            print(model)  # noqa: T201
            for quantizations in sizes.values():
                for slug in quantizations.values():
                    print(f"  - {slug}")  # noqa: T201
        return

    if args.command == "run":
        model_slug = args.model_slug or sorted(value for models in MODEL_MAPPING.values() for sizes in models.values() for value in sizes.values())[0]

        interface = WebLLMInterface(
            model_slug=model_slug,
            multiple_loads=args.multiple_loads,
        )
        pn.serve(interface, port=args.port, show=True)


if __name__ == "__main__":
    main()
