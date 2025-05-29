# llm-tools-mcp

[![PyPI](https://img.shields.io/pypi/v/llm-tools-mcp.svg)](https://pypi.org/project/llm-tools-mcp/)
[![Changelog](https://img.shields.io/github/v/release/rectalogic/llm-tools-mcp?include_prereleases&label=changelog)](https://github.com/rectalogic/llm-tools-mcp/releases)
[![Tests](https://github.com/rectalogic/llm-tools-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/rectalogic/llm-tools-mcp/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/rectalogic/llm-tools-mcp/blob/main/LICENSE)

MCP tools support

## Usage

To use this with the [LLM command-line tool](https://llm.datasette.io/en/stable/usage.html):

```bash
$ echo "The magic word is frumble" > magic.txt
$ uv run llm --tool 'MCP(command="npx", args=["-y", "@modelcontextprotocol/server-filesystem", "."])' "What is the magic word in the file ./magic.txt?" --tools-debug
Secure MCP Filesystem Server running on stdio
Allowed directories: [ '/Users/aw/Projects/rectalogic/llm-tools-mcp' ]

Tool call: read_file({'path': './magic.txt'})
  "CallToolResult(meta=None, content=[TextContent(type='text', text='The magic word is frumble\\n', annotations=None)], isError=False)"

The magic word in the file `magic.txt` is **frumble**.
```

With the [LLM Python API](https://llm.datasette.io/en/stable/python-api.html):

```python
import llm
from llm_tools_mcp import MCP

model = llm.get_model("gpt-4.1-mini")

result = model.chain(
    "Example prompt goes here",
    tools=[MCP(command="npx", args=["-y", "@modelcontextprotocol/server-filesystem", "."])]
).text()
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-tools-mcp
uv sync
```
To run the tests:
```bash
uv run pytest
```
