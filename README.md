# NVIDIA NIM Provider for Agent Zero

> Chat and embedding model provider plugin for [Agent Zero](https://github.com/agent0ai/agent-zero), powered by [NVIDIA NIM](https://build.nvidia.com) (NVIDIA Inference Microservice).

## Author

**[@shawn5cents](https://github.com/Shawn5cents)** — built for the [Agent Zero Plugin Hub](https://github.com/agent0ai/a0-plugins).

Issues and PRs welcome at the [plugin repo](https://github.com/Shawn5cents/agent-zero-nvidia-nim).

## Features

- **Chat models** — `nvidia_nim` chat provider (default `moonshotai/kimi-k2.6`)
- **Embedding models** — `nvidia_nim` embedding provider (default `nvidia/llama-nemotron-embed-1b-v2`)
- **Model discovery** — `/v1/models` enumeration in the Model Configuration UI
- **Self-hosted NIM** — override `api_base` to point at any NIM container or hosted endpoint (e.g. `http://host.docker.internal:8000/v1`)
- **Per-plugin key** — `NVIDIA_NIM_API_KEY` (set in Settings or as env var)
- **Examples** — see `examples/quickstart.py` for a zero-dependency demo of `/v1/models`, `/v1/chat/completions`, and `/v1/embeddings`

## Setup

1. Get a free API key at https://build.nvidia.com (free credits included).
2. In Agent Zero, open **Settings → External → NVIDIA NIM** and paste the key.
3. In **Settings → Agent**, set:
   - `chat_llm.provider` → `nvidia_nim`
   - `chat_llm.model_name` → `moonshotai/kimi-k2.6` (prebound default — 1T multimodal MoE)
   - `embedding_llm.provider` → `nvidia_nim`
   - `embedding_llm.model_name` → `nvidia/llama-nemotron-embed-1b-v2`
4. Restart the chat session.

## Top free-tier models (June 2026)

Defaults are tuned against the live `build.nvidia.com/models` free-endpoint catalog and refreshed on each release.

| Role | Recommended (default) | Strong alternates |
|---|---|---|
| **Reasoning / agentic chat** | `moonshotai/kimi-k2.6` | `openai/gpt-oss-120b`, `nvidia/nemotron-3-ultra-550b-a55b`, `meta/llama-4-maverick-17b-128e-instruct`, `deepseek-ai/deepseek-v4-pro`, `z-ai/glm-5.1`, `mistralai/mistral-large-3-675b-instruct-2512`, `qwen/qwen3.5-397b-a17b`, `nvidia/nemotron-3-super-120b-a12b`, `nvidia/nemotron-3-nano-30b-a3b`, `mistralai/mistral-medium-3.5-128b` |
| **Lightweight chat** | `openai/gpt-oss-20b` | `meta/llama-3.2-3b-instruct`, `meta/llama-3.2-1b-instruct`, `nvidia/nvidia-nemotron-nano-9b-v2`, `microsoft/phi-4-mini-instruct` |
| **Multimodal / vision** | `meta/llama-4-maverick-17b-128e-instruct` | `meta/llama-3.2-90b-vision-instruct`, `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`, `microsoft/phi-4-multimodal-instruct`, `qwen/qwen3.5-397b-a17b` |
| **Embedding (commercial)** | `nvidia/llama-nemotron-embed-1b-v2` | `nvidia/llama-3.2-nv-embedqa-1b-v1`, `baai/bge-m3`, `snowflake/arctic-embed-l` |
| **Embedding (SOTA, NC-only)** | `nvidia/nv-embed-v1` | `nvidia/nv-embedqa-mistral-7b-v2` |
| **Coding** | `deepseek-ai/deepseek-v4-pro` | `deepseek-ai/deepseek-v4-flash`, `qwen/qwen3.5-397b-a17b`, `mistralai/mistral-large-3-675b-instruct-2512` |

> Note: `nvidia/nv-embed-v1` is flagged **Non-Commercial Use Only** by NVIDIA. Pick `nvidia/llama-nemotron-embed-1b-v2` for production/commercial use.

## Self-hosted NIM

Run any NVIDIA NIM microservice (e.g. `Llama-3.1-70B-Instruct`) locally and override `api_base` in Settings → External → NVIDIA NIM:

```
http://host.docker.internal:8000/v1
```

The same `NVIDIA_NIM_API_KEY` setting works; for local containers you can leave the key empty (NIM does not require auth by default) or supply whatever header your proxy expects.

## Environment variable

The plugin reads `NVIDIA_NIM_API_KEY` directly when no settings key is provided. Useful for CI, Docker, or service-mode deployments.

```bash
export NVIDIA_NIM_API_KEY=nvapi-...
```

## Quickstart

```bash
git clone https://github.com/Shawn5cents/agent-zero-nvidia-nim
cd agent-zero-nvidia-nim
export NVIDIA_NIM_API_KEY=nvapi-...
python examples/quickstart.py
```

## License

MIT — see [LICENSE](LICENSE).
