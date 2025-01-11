# Examples

```{.python pycafe-embed pycafe-embed-style="border: 1px solid #e6e6e6; border-radius: 8px;" pycafe-embed-width="100%" pycafe-embed-height="400px" pycafe-embed-scale="1.0"}
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
template.servable()
```
