import panel as pn
import pytest

from panel_web_llm.main import WebLLM
from panel_web_llm.main import WebLLMInterface


class TestWebLLM:
    """Test suite for the WebLLM component."""

    @pytest.fixture
    def web_llm(self):
        """Create a basic WebLLM instance for testing."""
        return WebLLM()

    def test_initialization(self, web_llm):
        """Test initial state of WebLLM component."""
        assert not web_llm.loaded
        assert not web_llm.loading
        assert not web_llm.running
        assert web_llm.temperature == 1
        assert web_llm.history == 10
        assert web_llm.multiple_loads
        assert web_llm.load_status == {"text": "", "progress": 0}

    def test_model_select_initialization(self, web_llm):
        """Test model selection widget initialization."""
        assert web_llm._model_select.disabled is False
        assert web_llm._temperature_input.disabled is False
        assert web_llm._load_button.disabled is False
        assert "Load" in web_llm._load_button.name

    @pytest.mark.parametrize("loading_state", [True, False])
    def test_loading_state_controls(self, web_llm, loading_state):
        """Test control states during loading."""
        web_llm.loading = loading_state
        assert web_llm._model_select.disabled is loading_state
        assert web_llm._temperature_input.disabled is loading_state

    def test_load_button_state_changes(self, web_llm):
        """Test load button state changes."""
        web_llm.loaded = True
        assert web_llm._load_button.disabled is True
        assert web_llm._card.collapsed is True

        web_llm.loaded = False
        assert web_llm._load_button.disabled is False
        assert web_llm._card.visible is True

    def test_multiple_loads_behavior(self):
        """Test behavior when multiple loads is disabled."""
        web_llm = WebLLM(multiple_loads=False)
        web_llm.loaded = True

        assert web_llm._card.visible is False
        assert web_llm._load_button.disabled is True

        web_llm.loaded = False
        assert web_llm._card.visible is True
        assert web_llm._load_button.disabled is False

    def test_load_status_updates(self, web_llm):
        """Test load status updates during model loading."""
        web_llm.model_slug = "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC"
        web_llm.load_model = True

        assert web_llm.load_status["progress"] == 0
        assert "Preparing to load Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC" in web_llm.load_status["text"]

    async def test_completion_buffer_management(self, web_llm):
        """Test message buffer management during completions."""
        web_llm.running = True
        test_msg = {"finish_reason": None, "delta": {"content": "test"}}
        web_llm._handle_msg(test_msg)

        assert len(web_llm._buffer) == 1
        assert web_llm._buffer[0] == test_msg

        web_llm.running = False
        web_llm._buffer.clear()
        web_llm._handle_msg(test_msg)
        assert len(web_llm._buffer) == 0


class TestWebLLMInterface:
    """Test suite for the WebLLMInterface component."""

    @pytest.fixture
    def web_llm_interface(self):
        """Create a WebLLMInterface instance for testing."""
        return WebLLMInterface(model_slug="Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC")

    def test_initialization(self, web_llm_interface):
        """Test initial state of WebLLMInterface."""
        assert isinstance(web_llm_interface.web_llm, WebLLM)
        assert web_llm_interface.callback == web_llm_interface.web_llm.callback
        assert isinstance(web_llm_interface.header, pn.Column)

    def test_load_on_init_behavior(self):
        """Test behavior when load_on_init is enabled."""
        interface = WebLLMInterface(model_slug="Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC", load_on_init=True)

        assert len(interface.objects) == 0

        interface = WebLLMInterface(model_slug="Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC", load_on_init=False)

        assert hasattr(interface, "help_text")
        assert "Please first load the model" in interface.help_text

    def test_model_menu_visibility(self, web_llm_interface):
        """Test model menu visibility states."""
        assert web_llm_interface.web_llm.menu.visible is True

        web_llm_interface.web_llm.loaded = True
        web_llm_interface.web_llm.multiple_loads = False
        assert web_llm_interface.web_llm.menu.visible is False

    def test_initialization_with_params(self):
        """Test initialization with different parameters."""
        test_kwargs = {"system": "Test system prompt"}
        interface = WebLLMInterface(
            model_slug="Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC",
            multiple_loads=False,
            web_llm_kwargs=test_kwargs,
        )

        assert interface.web_llm.model_slug == "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC"
        assert interface.web_llm.multiple_loads is False
        assert interface.web_llm.system == "Test system prompt"

    @pytest.mark.parametrize("load_on_init", [True, False])
    def test_onload_behavior(self, load_on_init):
        """Test onload behavior with different configurations."""
        interface = WebLLMInterface(
            model_slug="Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC",
            load_on_init=load_on_init,
        )

        if load_on_init:
            assert len(interface.objects) == 0
        else:
            assert len(interface.objects) == 1
            assert "Please first load the model" in interface.help_text
