# Quickstart

`quickstart.py` is a zero-dependency demo of the three endpoints exposed by
the NVIDIA NIM provider plugin (chat, embeddings, list-models). It uses only
Python 3.9+ standard library, so it runs in any Agent Zero environment without
pip install.

```bash
export NVIDIA_NIM_API_KEY="nvapi-..."
python examples/quickstart.py
```

Expected output (abridged):

```
Using base URL: https://integrate.api.nvidia.com/v1

[1] Listing available models ...
    121 models available. First 5:
      - 01-ai/yi-large
      - abacusai/dracarys-llama-3.1-70b-instruct
      ...

[2] Chat completion via moonshotai/kimi-k2.6 ...
    Reply: NVIDIA NIM is NVIDIA's OpenAI-compatible inference microservice
    for serving foundation models on GPU infrastructure.

[3] Embedding via nvidia/llama-nemotron-embed-1b-v2 ...
    dim=2048  first 4 = [0.0123, -0.0456, 0.0789, -0.0234]

All three endpoints responded OK.
```

The defaults match the plugin's `default_config.yaml` pre-bindings:
- Chat: `moonshotai/kimi-k2.6`
- Embeddings: `nvidia/llama-nemotron-embed-1b-v2`
