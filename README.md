# llm-tools-mcp

[![PyPI](https://img.shields.io/pypi/v/llm-tools-mcp.svg)](https://pypi.org/project/llm-tools-mcp/)
[![Changelog](https://img.shields.io/github/v/release/rectalogic/llm-tools-mcp?include_prereleases&label=changelog)](https://github.com/rectalogic/llm-tools-mcp/releases)
[![Tests](https://github.com/rectalogic/llm-tools-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/rectalogic/llm-tools-mcp/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/rectalogic/llm-tools-mcp/blob/main/LICENSE)

MCP tools support

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-tools-mcp
```
## Usage

To use this with the [LLM command-line tool](https://llm.datasette.io/en/stable/usage.html):

```bash
llm --tool example_hello "Example prompt goes here" --tools-debug
```

With the [LLM Python API](https://llm.datasette.io/en/stable/python-api.html):

```python
import llm
from llm_tools_mcp import example_hello

model = llm.get_model("gpt-4.1-mini")

result = model.chain(
    "Example prompt goes here",
    tools=[example_hello]
).text()
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-tools-mcp
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
