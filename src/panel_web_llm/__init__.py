"""Accessible imports for the panel_web_llm package."""

import importlib.metadata
import warnings

from .main import WebLLM
from .main import WebLLMComponentMixin
from .main import WebLLMFeed
from .main import WebLLMInterface
from .models import ModelParam

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError as e:  # pragma: no cover
    warnings.warn(f"Could not determine version of {__name__}\n{e!s}", stacklevel=2)
    __version__ = "unknown"

__all__: list[str] = [
    "WebLLM",
    "WebLLMFeed",
    "WebLLMInterface",
    "WebLLMComponentMixin",
    "ModelParam",
]  # <- IMPORTANT FOR DOCS: fill with imports
