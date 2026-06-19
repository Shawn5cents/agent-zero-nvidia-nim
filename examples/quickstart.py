#!/usr/bin/env python3
"""
NVIDIA NIM Quickstart
======================

Self-contained demo of the three endpoints exposed by the NVIDIA NIM provider
plugin (chat, embeddings, list-models). Uses only the standard library + urllib,
so it runs in any Agent Zero environment without extra dependencies.

Setup:
    export NVIDIA_NIM_API_KEY="nvapi-..."
    # optional: override the host (defaults to https://integrate.api.nvidia.com)
    # export NVIDIA_NIM_BASE="http://host.docker.internal:8000/v1"

Run:
    python examples/quickstart.py
"""
import json
import os
import sys
import urllib.error
import urllib.request

API_KEY = os.environ.get("NVIDIA_NIM_API_KEY")
BASE    = os.environ.get("NVIDIA_NIM_BASE", "https://integrate.api.nvidia.com/v1")

def _request(method: str, path: str, body: dict | None = None) -> dict:
    url = f"{BASE}{path}"
    data = None
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    if body is not None:
        data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def list_models() -> list[str]:
    print("\n[1] Listing available models ...")
    r = _request("GET", "/models")
    ids = sorted(m["id"] for m in r.get("data", r) if isinstance(m, dict) and "id" in m)
    print(f"    {len(ids)} models available. First 5:")
    for m in ids[:5]:
        print(f"      - {m}")
    return ids

def chat(model: str, prompt: str) -> str:
    print(f"\n[2] Chat completion via {model} ...")
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256,
        "temperature": 0.2,
    }
    r = _request("POST", "/chat/completions", body)
    msg = r["choices"][0]["message"]["content"]
    print(f"    Reply: {msg[:200]}{'...' if len(msg) > 200 else ''}")
    return msg

def embed(model: str, text: str) -> list[float]:
    print(f"\n[3] Embedding via {model} ...")
    body = {"model": model, "input": text}
    r = _request("POST", "/embeddings", body)
    vec = r["data"][0]["embedding"]
    print(f"    dim={len(vec)}  first 4 = {vec[:4]}")
    return vec

def main() -> int:
    if not API_KEY:
        print("WARNING: NVIDIA_NIM_API_KEY is not set.", file=sys.stderr)
        print("         Set it via env var or paste into the plugin settings UI.",
              file=sys.stderr)
    print(f"Using base URL: {BASE}")

    list_models()
    chat("moonshotai/kimi-k2.6",
         "In one sentence, what does NVIDIA NIM provide?")
    embed("nvidia/llama-nemotron-embed-1b-v2",
          "NVIDIA NIM is an OpenAI-compatible inference microservice.")

    print("\nAll three endpoints responded OK.\n")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} {e.reason}: {e.read().decode(errors='replace')}",
              file=sys.stderr)
        sys.exit(1)
