import llm


def example_hello(input: str) -> str:
    """
    Description of tool goes here.
    """
    return f"hello {input}"


@llm.hookimpl
def register_tools(register):
    register(example_hello)
