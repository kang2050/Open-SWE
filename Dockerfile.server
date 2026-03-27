FROM python:3.12-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl build-essential openssh-client jq \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Copy project files first for better layer caching
COPY pyproject.toml uv.lock langgraph.json ./

# Install dependencies
RUN uv pip install --system -e . 2>/dev/null || uv pip install --system \
    "deepagents>=0.4.3" \
    "fastapi>=0.104.0" \
    "uvicorn>=0.24.0" \
    "httpx>=0.25.0" \
    "PyJWT>=2.8.0" \
    "cryptography>=41.0.0" \
    "langgraph-sdk>=0.1.0" \
    "langchain>=1.2.9" \
    "langgraph>=1.0.8" \
    "markdownify>=1.2.2" \
    "langchain-anthropic>1.1.0" \
    "langgraph-cli[inmem]>=0.4.12" \
    "langsmith>=0.7.1" \
    "langchain-openai==1.1.10" \
    "exa-py>=2.10.1"

# Copy full source
COPY . .

# Install the package itself
RUN uv pip install --system -e .

# Create workspace directory for local sandbox
RUN mkdir -p /tmp/open-swe-workspace

EXPOSE 8000

# Run LangGraph dev server (in-memory mode, suitable for trial)
CMD ["langgraph", "dev", "--host", "0.0.0.0", "--port", "8000", "--no-browser"]
