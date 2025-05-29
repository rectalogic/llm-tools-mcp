import json
import os

import llm

from llm_tools_mcp import MCP

ROOT = os.path.join(os.path.dirname(__file__), "..")

def test_tool():
    model = llm.get_model("echo")
    toolbox = MCP(command="npx", args=["-y", "@modelcontextprotocol/server-filesystem", ROOT])
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {"name": "read_file", "arguments": {"path": "./LICENSE"}}
                ]
            }
        ),
        tools=list(toolbox.method_tools()),
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results[0]["name"] == "read_file"
    assert "Apache License" in tool_results[0]["output"]
