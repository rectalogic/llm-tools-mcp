import asyncio
from contextlib import AsyncExitStack

import llm
import mcp
from mcp.client.stdio import stdio_client


class MCP(llm.Toolbox):
    """MCP tool support"""

    def __init__(self, command: str, args: list[str] | None = None):
        self.exit_stack = AsyncExitStack()
        self.runner = self.exit_stack.enter_context(asyncio.Runner())
        self.runner.run(self._initialize(command, args))

    async def _initialize(self, command: str, args: list[str] | None = None):
        server_params = mcp.StdioServerParameters(
            command=command,
            args=args,
            env=None,
        )
        read, write = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        self.session = await self.exit_stack.enter_async_context(
            mcp.ClientSession(read, write)
        )
        await self.session.initialize()
        self.tools = [
            self._convert_tool(tool) for tool in (await self.session.list_tools()).tools
        ]

    def _convert_tool(self, tool: mcp.Tool) -> llm.Tool:
        async def async_implementation(**kwargs):
            return await self.session.call_tool(tool.name, arguments=kwargs)

        def implementation(**kwargs):
            return self.runner.run(async_implementation(**kwargs))

        return llm.Tool(
            name=tool.name,
            description=tool.description,
            input_schema=tool.inputSchema,
            implementation=implementation,
            plugin="MCP",
        )

    def tools_not_yet_available(self):
        """MCP tools are available at runtime"""

    def method_tools(self):
        yield from iter(self.tools)


@llm.hookimpl
def register_tools(register):
    register(MCP)
