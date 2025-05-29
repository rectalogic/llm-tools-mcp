import llm
import json
from llm_tools_mcp import example_hello


def test_tool():
    model = llm.get_model("echo")
    chain_response = model.chain(
        json.dumps(
            {
                "tool_calls": [
                    {"name": "example_hello", "arguments": {"input": "pelican"}}
                ]
            }
        ),
        tools=[example_hello],
    )
    responses = list(chain_response.responses())
    tool_results = json.loads(responses[-1].text())["tool_results"]
    assert tool_results == [
        {"name": "example_hello", "output": "hello pelican", "tool_call_id": None}
    ]
