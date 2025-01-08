import pytest
from panel.widgets import NestedSelect

from panel_web_llm.models import ModelParam


class TestModelParam:
    """Test suite for the ModelParam class."""

    @pytest.fixture
    def levels(self):
        """Standard levels configuration for NestedSelect widget."""
        return [
            {"name": "Model", "sizing_mode": "stretch_width"},
            {"name": "Size", "sizing_mode": "stretch_width"},
            {"name": "Quantization", "sizing_mode": "stretch_width"},
        ]

    @pytest.fixture
    def model_mapping(self):
        """Standard model mapping configuration."""
        return {
            "Qwen2.5-Coder": {"0.5B": {"q0f16": "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC"}},
            "gemma-2": {"27b": {"q0f16": "gemma-2-27b-it-q0f16-MLC"}},
        }

    def test_initialization(self):
        """Verify clean initialization with valid parameters."""
        param = ModelParam(model="Qwen2.5-Coder", size="0.5B", quantization="q0f16")
        assert param.model == "Qwen2.5-Coder"
        assert param.size == "0.5B"
        assert param.quantization == "q0f16"

    def test_lookup_model_slug(self, model_mapping):
        """Test model slug lookup functionality."""
        param = ModelParam(model="Qwen2.5-Coder", size="0.5B", quantization="q0f16")
        assert param.lookup_model_slug(model_mapping) == "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC"

    def test_to_dict_with_dict_levels(self, levels):
        """Test dictionary conversion with standard levels structure."""
        param = ModelParam(model="Qwen2.5-Coder", size="0.5B", quantization="q0f16")
        result = param.to_dict(levels)
        assert result == {
            "Model": "Qwen2.5-Coder",
            "Size": "0.5B",
            "Quantization": "q0f16",
        }

    def test_to_dict_with_list_levels(self):
        """Test dictionary conversion with simple list levels."""
        levels = ["Model", "Size", "Quantization"]
        param = ModelParam(model="Qwen2.5-Coder", size="0.5B", quantization="q0f16")
        result = param.to_dict(levels)
        assert result == {
            "Model": "Qwen2.5-Coder",
            "Size": "0.5B",
            "Quantization": "q0f16",
        }

    def test_from_nested_select(self, levels):
        """Test creation from NestedSelect widget."""
        select = NestedSelect(
            name="Model Select",
            value={"Model": "Qwen2.5-Coder", "Size": "0.5B", "Quantization": "q0f16"},
            options={
                "Qwen2.5-Coder": {"0.5B": ["q0f16"]},
                "gemma-2": {"27b": ["q0f16"]},
            },
            levels=levels,
        )
        param = ModelParam.from_nested_select(select)
        assert param.model == "Qwen2.5-Coder"
        assert param.size == "0.5B"
        assert param.quantization == "q0f16"

    @pytest.mark.parametrize(
        "slug,expected",
        [
            (
                "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC",
                ("Qwen2.5-Coder", "0.5B", "q0f16"),
            ),
            ("gemma-2-27b-it-q0f16-MLC", ("gemma-2", "27b", "q0f16")),
            ("model-without-size-q0f16-MLC", ("model-without-size", "-", "q0f16")),
            ("model-1.5B-q0f16-MLC", ("model", "1.5B", "q0f16")),
            ("model-500M-q0f16-MLC", ("model", "500M", "q0f16")),
        ],
    )
    def test_from_model_slug(self, slug, expected):
        """Test model slug parsing with various formats."""
        param = ModelParam.from_model_slug(slug)
        assert param.model == expected[0]
        assert param.size == expected[1]
        assert param.quantization == expected[2]
