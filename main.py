from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Campus Lost & Found")

LOST_FILE = os.path.join(os.path.dirname(__file__), "lost.txt")
FOUND_FILE = os.path.join(os.path.dirname(__file__), "found.txt")

def ensure_files():
    for f in [LOST_FILE, FOUND_FILE]:
        if not os.path.exists(f):
            with open(f, "w") as file:
                file.write("")

@mcp.tool()
def report_lost(item: str) -> str:
    """
    Log a lost item to lost.txt.
    """
    ensure_files()
    with open(LOST_FILE, "a") as f:
        f.write(item + "\n")
    return f"✅ Lost item reported: '{item}'"

@mcp.tool()
def report_found(item: str) -> str:
    """
    Log a found item to found.txt.
    """
    ensure_files()
    with open(FOUND_FILE, "a") as f:
        f.write(item + "\n")
    return f"✅ Found item reported: '{item}'"

@mcp.tool()
def show_lost() -> str:
    """
    Return all reported lost items.
    """
    ensure_files()
    with open(LOST_FILE, "r") as f:
        content = f.read().strip()
    return content or "📭 No lost items reported."

@mcp.tool()
def show_found() -> str:
    """
    Return all reported found items.
    """
    ensure_files()
    with open(FOUND_FILE, "r") as f:
        content = f.read().strip()
    return content or "📬 No found items reported."

@mcp.resource("lost://latest")
def latest_lost() -> str:
    """
    Get the most recent lost item.
    """
    ensure_files()
    with open(LOST_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "📭 No lost items reported."

@mcp.resource("found://latest")
def latest_found() -> str:
    """
    Get the most recent found item.
    """
    ensure_files()
    with open(FOUND_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "📬 No found items reported."

@mcp.prompt()
def summary_prompt() -> str:
    """
    Generate a prompt asking AI to summarize current lost and found items.
    """
    ensure_files()
    with open(LOST_FILE, "r") as lf, open(FOUND_FILE, "r") as ff:
        lost = lf.read().strip()
        found = ff.read().strip()
    
    if not lost and not found:
        return "There are no lost or found items to summarize."
    
    prompt = "Summarize the campus lost and found records.\n"
    if lost:
        prompt += f"Lost Items:\n{lost}\n"
    if found:
        prompt += f"Found Items:\n{found}\n"
    return prompt
if __name__ == "__main__":
    mcp.run()
