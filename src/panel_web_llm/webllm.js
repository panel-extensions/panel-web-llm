import * as webllm from "https://esm.run/@mlc-ai/web-llm";

const engines = new Map()

export async function render({ model }) {
  model.on("msg:custom", async (event) => {
    if (event.type === 'load') {
      model.loading = true
      if (!engines.has(model.model_slug)) {
        const initProgressCallback = (load_status) => {
          // Parse progress from cache loading messages like "[43/88]"
          const match = load_status.text.match(/\[(\d+)\/(\d+)\]/)
          if (match) {
            const [_, current, total] = match
            load_status.progress = current / total
          }
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
          console.warn(error.message)
          model.load_status = {
            progress: 0,
            text: error.message + " Try again later, or try a different size/quantization.",
          };
          model.loaded = false
        }
      }
      model.loading = false
    } else if (event.type === 'completion') {
      const engine = engines.get(model.model_slug)
      if (engine == null) {
        model.send_msg({'finish_reason': 'error'})
        return
      }
      model.running = true
      const format = event.response_format
      const chunks = await engine.chat.completions.create({
        messages: event.messages,
        temperature: model.temperature,
        response_format: format ? { type: format.type, schema: format.schema ? JSON.stringify(format.schema) : undefined } : undefined,
        stream: event.stream,
      })
      if (event.stream) {
        let buffer = ""
        let current = null
        let lastChunk = null
        let timeout = null
        const sendBuffer = () => {
          if (buffer) {
            console.log(buffer)
            model.send_msg({
              delta: { content: buffer, role: current.delta.role },
              index: current.index,
              finish_reason: null
            })
            buffer = "";
          }
          if (lastChunk && lastChunk.finish_reason) {
            model.send_msg(lastChunk)
            lastChunk = null
          }
        }
        timeout = setInterval(sendBuffer, 200)
        for await (const chunk of chunks) {
          if (!model.running) {
            break
          }
          const choice = chunk.choices[0]
          if (choice.delta.content) {
            current = choice
            buffer += choice.delta.content;
          }
          if (choice.finish_reason) {
            lastChunk = choice;
          }
        }
        clearTimeout(timeout)
        sendBuffer()
      } else {
        model.send_msg(chunks.choices[0])
      }
    }
  })
}
