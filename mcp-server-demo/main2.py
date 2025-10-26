from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("AI Sticky Notes")
NOTES_FILE = "notes.txt"

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

## Decorator
@mcp.tool()
def add_note(message: str) -> str:
    """

    :param message:
    :return:
    """


    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note served"


