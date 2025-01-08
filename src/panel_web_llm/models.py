"""A module to define a ModelParam class for model parameters."""

from __future__ import annotations

import re

import panel as pn
import param


class ModelParam(param.Parameterized):
    """A class to represent model parameters including model name, size, and quantization.

    This class provides methods to lookup model slugs based on mappings, convert parameters
    to dictionaries, and create instances from nested selects or model slugs.
    """

    model = param.String(doc="The model name.")
    """The name of the model."""

    size = param.String(doc="The size of the model.")
    """The size of the model, e.g., '7B', '13B', etc."""

    quantization = param.String(doc="The quantization of the model.")
    """The quantization applied to the model, e.g., 'AWQ', 'GPTQ'."""

    def lookup_model_slug(self, model_mapping: dict) -> str:
        """Looks up the model slug based on the given model mapping.

        Args:
            model_mapping (dict): A nested dictionary mapping model name, size, and quantization to a model slug.

        Returns
        -------
            str: The model slug corresponding to the current model parameters.
        """
        return model_mapping[self.model][self.size][self.quantization]

    def to_dict(self, levels: list) -> dict:
        """Converts the model parameters to a dictionary.

        Args:
            levels (list): A list of keys or dictionaries defining how the parameters should be structured in the output dictionary.
                           If the levels are strings they will be used as keys. If the levels are dictionaries, the 'name' key
                           will be used as key.

        Returns
        -------
            dict: A dictionary representation of the model parameters.
        """
        if not isinstance(levels[0], dict):
            return {
                levels[0]: self.model,
                levels[1]: self.size,
                levels[2]: self.quantization,
            }
        return {
            levels[0]["name"]: self.model,
            levels[1]["name"]: self.size,
            levels[2]["name"]: self.quantization,
        }

    @classmethod
    def from_nested_select(cls, nested_select: pn.widgets.NestedSelect) -> "ModelParam":
        """Creates a ModelParam instance from a NestedSelect widget.

        Args:
            nested_select (pn.widgets.NestedSelect): The NestedSelect widget containing the model parameters.

        Returns
        -------
            ModelParam: A ModelParam instance initialized with the values from the NestedSelect.
        """
        value = nested_select.value
        levels = nested_select.levels
        if not isinstance(levels[0], dict):
            return cls(
                model=value[levels[0]],
                size=value[levels[1]],
                quantization=value[levels[2]],
            )
        return cls(
            model=value[levels[0]["name"]],
            size=value[levels[1]["name"]],
            quantization=value[levels[2]["name"]],
        )

    @classmethod
    def from_model_slug(cls, model_slug: str) -> "ModelParam":
        """Creates a ModelParam instance from a model slug string.

        Args:
            model_slug (str): The model slug string, e.g., 'llama-7B-AWQ'.

        Returns
        -------
            ModelParam: A ModelParam instance initialized with the parsed values from the model slug.
        """
        model_label, model_quantization, _ = model_slug.rsplit("-", 2)
        model_parameters_re = re.search(r"\d+(\.\d+)?[BbKkmM]", model_label)
        if model_parameters_re:
            model_parameters = model_parameters_re.group(0)
            model_name = model_label[: model_parameters_re.start()].rstrip("-").rstrip("_")
        else:
            model_parameters = "-"
            model_name = model_label.rstrip("-").rstrip("_")
        return cls(model=model_name, size=model_parameters, quantization=model_quantization)
