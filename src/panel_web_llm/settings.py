"""Config settings."""

MODEL_MAPPING = {
    "Llama-3": {
        "8B": {
            "q0f16": "Llama-3-8B-Instruct-q0f16-MLC",
            "q3f16_1": "Llama-3-8B-Instruct-q3f16_1-MLC",
            "q4f16_1": "Llama-3-8B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Llama-3-8B-Instruct-q4f32_1-MLC",
        }
    },
    "Llama-3.1": {
        "70B": {
            "q0f16": "Llama-3.1-70B-Instruct-q0f16-MLC",
            "q3f16_1": "Llama-3.1-70B-Instruct-q3f16_1-MLC",
            "q4f16_1": "Llama-3.1-70B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Llama-3.1-70B-Instruct-q4f32_1-MLC",
        },
        "8B": {
            "q0f16": "Llama-3.1-8B-Instruct-q0f16-MLC",
            "q4f16_1": "Llama-3.1-8B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Llama-3.1-8B-Instruct-q4f32_1-MLC",
            "q3f16_0": "Llama-3.1-8B-Instruct-q3f16_0-MLC",
            "q3f16_1": "Llama-3.1-8B-Instruct-q3f16_1-MLC",
        },
    },
    "Llama-3.2": {
        "1B": {
            "q0f16": "Llama-3.2-1B-Instruct-q0f16-MLC",
            "q0f32": "Llama-3.2-1B-Instruct-q0f32-MLC",
            "q4f16_0": "Llama-3.2-1B-Instruct-q4f16_0-MLC",
            "q4f16_1": "Llama-3.2-1B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Llama-3.2-1B-Instruct-q4f32_1-MLC",
        },
        "3B": {
            "q0f16": "Llama-3.2-3B-Instruct-q0f16-MLC",
            "q0f32": "Llama-3.2-3B-Instruct-q0f32-MLC",
            "q4f16_0": "Llama-3.2-3B-Instruct-q4f16_0-MLC",
            "q4f16_1": "Llama-3.2-3B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Llama-3.2-3B-Instruct-q4f32_1-MLC",
        },
    },
    "Hermes-2-Pro-Llama-3": {
        "8B": {
            "q0f16": "Hermes-2-Pro-Llama-3-8B-q0f16-MLC",
            "q3f16_1": "Hermes-2-Pro-Llama-3-8B-q3f16_1-MLC",
            "q4f16_1": "Hermes-2-Pro-Llama-3-8B-q4f16_1-MLC",
            "q4f32_1": "Hermes-2-Pro-Llama-3-8B-q4f32_1-MLC",
        }
    },
    "Hermes-2-Theta-Llama-3": {
        "70B": {
            "q0f16": "Hermes-2-Theta-Llama-3-70B-q0f16-MLC",
            "q3f16_1": "Hermes-2-Theta-Llama-3-70B-q3f16_1-MLC",
            "q4f16_1": "Hermes-2-Theta-Llama-3-70B-q4f16_1-MLC",
            "q4f32_1": "Hermes-2-Theta-Llama-3-70B-q4f32_1-MLC",
        },
        "8B": {
            "q0f16": "Hermes-2-Theta-Llama-3-8B-q0f16-MLC",
            "q3f16_1": "Hermes-2-Theta-Llama-3-8B-q3f16_1-MLC",
            "q4f16_1": "Hermes-2-Theta-Llama-3-8B-q4f16_1-MLC",
            "q4f32_1": "Hermes-2-Theta-Llama-3-8B-q4f32_1-MLC",
        },
    },
    "Hermes-3-Llama-3.1": {
        "8B": {
            "q0f16": "Hermes-3-Llama-3.1-8B-q0f16-MLC",
            "q3f16_1": "Hermes-3-Llama-3.1-8B-q3f16_1-MLC",
            "q4f16_1": "Hermes-3-Llama-3.1-8B-q4f16_1-MLC",
            "q4f32_1": "Hermes-3-Llama-3.1-8B-q4f32_1-MLC",
        }
    },
    "Hermes-3-Llama-3.2": {
        "3B": {
            "q0f16": "Hermes-3-Llama-3.2-3B-q0f16-MLC",
            "q4f16_1": "Hermes-3-Llama-3.2-3B-q4f16_1-MLC",
            "q4f32_1": "Hermes-3-Llama-3.2-3B-q4f32_1-MLC",
        }
    },
    "Phi-3-mini": {
        "128k": {
            "q0f16": "Phi-3-mini-128k-instruct-q0f16-MLC",
            "q4f16_1": "Phi-3-mini-128k-instruct-q4f16_1-MLC",
            "q4f32_1": "Phi-3-mini-128k-instruct-q4f32_1-MLC",
        }
    },
    "Phi-3.5-mini-instruct": {
        "-": {
            "q0f16": "Phi-3.5-mini-instruct-q0f16-MLC",
            "q4f16_0": "Phi-3.5-mini-instruct-q4f16_0-MLC",
            "q4f16_1": "Phi-3.5-mini-instruct-q4f16_1-MLC",
            "q4f32_1": "Phi-3.5-mini-instruct-q4f32_1-MLC",
        }
    },
    "Phi-3.5-vision-instruct": {
        "-": {
            "q0f16": "Phi-3.5-vision-instruct-q0f16-MLC",
            "q3f16_1": "Phi-3.5-vision-instruct-q3f16_1-MLC",
            "q4f16_1": "Phi-3.5-vision-instruct-q4f16_1-MLC",
            "q4f32_1": "Phi-3.5-vision-instruct-q4f32_1-MLC",
        }
    },
    "Mistral": {
        "7B": {
            "q0f16": "Mistral-7B-Instruct-v0.3-q0f16-MLC",
            "q3f16_1": "Mistral-7B-Instruct-v0.3-q3f16_1-MLC",
            "q4f16_0": "Mistral-7B-Instruct-v0.3-q4f16_0-MLC",
            "q4f16_1": "Mistral-7B-Instruct-v0.3-q4f16_1-MLC",
            "q4f32_1": "Mistral-7B-Instruct-v0.3-q4f32_1-MLC",
        }
    },
    "Qwen1.5": {
        "0.5B": {
            "q0f16": "Qwen1.5-0.5B-Chat-q0f16-MLC",
            "q4f16_1": "Qwen1.5-0.5B-Chat-q4f16_1-MLC",
            "q4f32_1": "Qwen1.5-0.5B-Chat-q4f32_1-MLC",
        },
        "1.8B": {
            "q0f16": "Qwen1.5-1.8B-Chat-q0f16-MLC",
            "q4f16_1": "Qwen1.5-1.8B-Chat-q4f16_1-MLC",
            "q4f32_1": "Qwen1.5-1.8B-Chat-q4f32_1-MLC",
        },
    },
    "Qwen2": {
        "0.5B": {
            "q0f16": "Qwen2-0.5B-Instruct-q0f16-MLC",
            "q0f32": "Qwen2-0.5B-Instruct-q0f32-MLC",
            "q4f16_0": "Qwen2-0.5B-Instruct-q4f16_0-MLC",
            "q4f16_1": "Qwen2-0.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-0.5B-Instruct-q4f32_1-MLC",
        },
        "1.5B": {
            "q0f16": "Qwen2-1.5B-Instruct-q0f16-MLC",
            "q4f16_0": "Qwen2-1.5B-Instruct-q4f16_0-MLC",
            "q4f16_1": "Qwen2-1.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-1.5B-Instruct-q4f32_1-MLC",
        },
        "72B": {
            "q0f16": "Qwen2-72B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2-72B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-72B-Instruct-q4f32_1-MLC",
        },
        "7B": {
            "q0f16": "Qwen2-7B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2-7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-7B-Instruct-q4f32_1-MLC",
        },
    },
    "Qwen2-Math": {
        "1.5B": {
            "q0f16": "Qwen2-Math-1.5B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2-Math-1.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-Math-1.5B-Instruct-q4f32_1-MLC",
        },
        "72B": {
            "q0f16": "Qwen2-Math-72B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2-Math-72B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-Math-72B-Instruct-q4f32_1-MLC",
        },
        "7B": {
            "q0f16": "Qwen2-Math-7B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2-Math-7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2-Math-7B-Instruct-q4f32_1-MLC",
        },
    },
    "Qwen2.5": {
        "0.5B": {
            "q0f16": "Qwen2.5-0.5B-Instruct-q0f16-MLC",
            "q0f32": "Qwen2.5-0.5B-Instruct-q0f32-MLC",
            "q4f16_1": "Qwen2.5-0.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-0.5B-Instruct-q4f32_1-MLC",
        },
        "1.5B": {
            "q0f16": "Qwen2.5-1.5B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-1.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-1.5B-Instruct-q4f32_1-MLC",
        },
        "14B": {
            "q0f16": "Qwen2.5-14B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-14B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-14B-Instruct-q4f32_1-MLC",
        },
        "32B": {
            "q0f16": "Qwen2.5-32B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-32B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-32B-Instruct-q4f32_1-MLC",
        },
        "3B": {
            "q0f16": "Qwen2.5-3B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-3B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-3B-Instruct-q4f32_1-MLC",
        },
        "72B": {
            "q0f16": "Qwen2.5-72B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-72B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-72B-Instruct-q4f32_1-MLC",
        },
        "7B": {
            "q0f16": "Qwen2.5-7B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-7B-Instruct-q4f32_1-MLC",
        },
    },
    "Qwen2.5-Coder": {
        "0.5B": {
            "q0f16": "Qwen2.5-Coder-0.5B-Instruct-q0f16-MLC",
            "q0f32": "Qwen2.5-Coder-0.5B-Instruct-q0f32-MLC",
            "q4f16_0": "Qwen2.5-Coder-0.5B-Instruct-q4f16_0-MLC",
            "q4f16_1": "Qwen2.5-Coder-0.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-0.5B-Instruct-q4f32_1-MLC",
        },
        "1.5B": {
            "q0f16": "Qwen2.5-Coder-1.5B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Coder-1.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-1.5B-Instruct-q4f32_1-MLC",
        },
        "14B": {
            "q0f16": "Qwen2.5-Coder-14B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Coder-14B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-14B-Instruct-q4f32_1-MLC",
        },
        "32B": {
            "q0f16": "Qwen2.5-Coder-32B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Coder-32B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-32B-Instruct-q4f32_1-MLC",
        },
        "3B": {
            "q0f16": "Qwen2.5-Coder-3B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Coder-3B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-3B-Instruct-q4f32_1-MLC",
        },
        "7B": {
            "q0f16": "Qwen2.5-Coder-7B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Coder-7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Coder-7B-Instruct-q4f32_1-MLC",
        },
    },
    "Qwen2.5-Math": {
        "1.5B": {
            "q0f16": "Qwen2.5-Math-1.5B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Math-1.5B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Math-1.5B-Instruct-q4f32_1-MLC",
        },
        "72B": {
            "q0f16": "Qwen2.5-Math-72B-Instruct-q0f16-MLC",
            "q4f16_1": "Qwen2.5-Math-72B-Instruct-q4f16_1-MLC",
            "q4f32_1": "Qwen2.5-Math-72B-Instruct-q4f32_1-MLC",
        },
    },
    "DeepSeek-R1-Distill-Llama": {
        "70B": {
            "q0f16": "DeepSeek-R1-Distill-Llama-70B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Llama-70B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Llama-70B-q4f32_1-MLC",
        },
        "8B": {
            "q0f16": "DeepSeek-R1-Distill-Llama-8B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Llama-8B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Llama-8B-q4f32_1-MLC",
        },
    },
    "DeepSeek-R1-Distill-Qwen": {
        "1.5B": {
            "q0f16": "DeepSeek-R1-Distill-Qwen-1.5B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Qwen-1.5B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Qwen-1.5B-q4f32_1-MLC",
        },
        "14B": {
            "q0f16": "DeepSeek-R1-Distill-Qwen-14B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Qwen-14B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Qwen-14B-q4f32_1-MLC",
        },
        "32B": {
            "q0f16": "DeepSeek-R1-Distill-Qwen-32B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Qwen-32B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Qwen-32B-q4f32_1-MLC",
        },
        "7B": {
            "q0f16": "DeepSeek-R1-Distill-Qwen-7B-q0f16-MLC",
            "q4f16_1": "DeepSeek-R1-Distill-Qwen-7B-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-R1-Distill-Qwen-7B-q4f32_1-MLC",
        },
    },
    "DeepSeek-V2-Lite-Chat": {
        "-": {
            "q0f16": "DeepSeek-V2-Lite-Chat-q0f16-MLC",
            "q4f16_1": "DeepSeek-V2-Lite-Chat-q4f16_1-MLC",
            "q4f32_1": "DeepSeek-V2-Lite-Chat-q4f32_1-MLC",
        }
    },
    "Mixtral-8x": {
        "7B": {
            "q0f16": "Mixtral-8x7B-Instruct-v0.1-q0f16-MLC",
            "q4f16_1": "Mixtral-8x7B-Instruct-v0.1-q4f16_1-MLC",
            "q4f32_1": "Mixtral-8x7B-Instruct-v0.1-q4f32_1-MLC",
        }
    },
    "SmolLM": {
        "1.7B": {
            "q0f16": "SmolLM-1.7B-Instruct-q0f16-MLC",
            "q0f32": "SmolLM-1.7B-Instruct-q0f32-MLC",
            "q4f16_1": "SmolLM-1.7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM-1.7B-Instruct-q4f32_1-MLC",
        },
        "135M": {
            "q0f16": "SmolLM-135M-Instruct-q0f16-MLC",
            "q0f32": "SmolLM-135M-Instruct-q0f32-MLC",
            "q4f16_1": "SmolLM-135M-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM-135M-Instruct-q4f32_1-MLC",
        },
        "360M": {
            "q0f16": "SmolLM-360M-Instruct-q0f16-MLC",
            "q0f32": "SmolLM-360M-Instruct-q0f32-MLC",
            "q4f16_1": "SmolLM-360M-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM-360M-Instruct-q4f32_1-MLC",
        },
    },
    "SmolLM2": {
        "1.7B": {
            "q0f16": "SmolLM2-1.7B-Instruct-q0f16-MLC",
            "q4f16_1": "SmolLM2-1.7B-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM2-1.7B-Instruct-q4f32_1-MLC",
        },
        "135M": {
            "q0f16": "SmolLM2-135M-Instruct-q0f16-MLC",
            "q0f32": "SmolLM2-135M-Instruct-q0f32-MLC",
            "q4f16_1": "SmolLM2-135M-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM2-135M-Instruct-q4f32_1-MLC",
        },
        "360M": {
            "q0f16": "SmolLM2-360M-Instruct-q0f16-MLC",
            "q0f32": "SmolLM2-360M-Instruct-q0f32-MLC",
            "q4f16_1": "SmolLM2-360M-Instruct-q4f16_1-MLC",
            "q4f32_1": "SmolLM2-360M-Instruct-q4f32_1-MLC",
        },
    },
    "gemma-2": {
        "27b": {
            "q0f16": "gemma-2-27b-it-q0f16-MLC",
            "q4f16_1": "gemma-2-27b-it-q4f16_1-MLC",
            "q4f32_1": "gemma-2-27b-it-q4f32_1-MLC",
        },
        "2b": {
            "q0f16": "gemma-2-2b-jpn-it-q0f16-MLC",
            "q0f32": "gemma-2-2b-jpn-it-q0f32-MLC",
            "q4f16_0": "gemma-2-2b-it-q4f16_0-MLC",
            "q4f16_1": "gemma-2-2b-jpn-it-q4f16_1-MLC",
            "q4f32_1": "gemma-2-2b-jpn-it-q4f32_1-MLC",
        },
        "9b": {
            "q0f16": "gemma-2-9b-it-q0f16-MLC",
            "q3f16_1": "gemma-2-9b-it-q3f16_1-MLC",
            "q4f16_1": "gemma-2-9b-it-q4f16_1-MLC",
            "q4f32_1": "gemma-2-9b-it-q4f32_1-MLC",
        },
    },
    "internlm2_5-1": {
        "8b": {
            "q0f16": "internlm2_5-1_8b-chat-q0f16-MLC",
            "q4f16_1": "internlm2_5-1_8b-chat-q4f16_1-MLC",
            "q4f32_1": "internlm2_5-1_8b-chat-q4f32_1-MLC",
        }
    },
    "internlm2_5": {
        "20b": {
            "q0f16": "internlm2_5-20b-chat-q0f16-MLC",
            "q4f16_1": "internlm2_5-20b-chat-q4f16_1-MLC",
            "q4f32_1": "internlm2_5-20b-chat-q4f32_1-MLC",
        },
        "7b": {
            "q0f16": "internlm2_5-7b-chat-q0f16-MLC",
            "q4f16_1": "internlm2_5-7b-chat-q4f16_1-MLC",
            "q4f32_1": "internlm2_5-7b-chat-q4f32_1-MLC",
        },
    },
}
