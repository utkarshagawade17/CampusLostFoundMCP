# 🎒 Campus Lost & Found MCP Server

A Claude Desktop-compatible MCP (Model Context Protocol) server that lets users report, track, and summarize lost and found items on campus via a simple CLI or LLM interface.

---

## 🚀 Features

- Report lost or found items
- View lists of reported items
- Fetch the latest lost/found item
- Generate a summary prompt for Claude to reason about
- Persistent storage using local text files
- Works seamlessly with Claude Desktop (Anthropic)

---

## 📁 Project Structure

CampusLostFoundMCP/
├── main.py # MCP server definition using FastMCP
├── lost.txt # Stores lost item entries (auto-created)
├── found.txt # Stores found item entries (auto-created)
├── pyproject.toml # uv/mcp environment config
├── uv.lock # Dependency lock file
└── README.md


---

## 🧪 Tool Functions

These can be called directly inside Claude Desktop:

```python
report_lost("wallet near cafeteria")
report_found("blue bottle in gym")
show_lost()
show_found()
latest_lost()
latest_found()
summary_prompt()
```

🛠️ Setup Instructions
1. Clone the repository:

   `git clone https://github.com/<your-username>/CampusLostFoundMCP.git
    cd CampusLostFoundMCP`

2. Ensure Python 3.11+ is installed

3. Install dependencies:

   `uv init .
    uv add "mcp[cli]" `

4. Run the server:

   `uv run main.py`

🧩 Claude Desktop Integration

Add the following to your claude_desktop_config.json:

`{
  "mcpServers": {
    "Campus Lost & Found": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/CampusLostFoundMCP",
        "run",
        "main.py"
      ]
    }
  }
}
`

📬 Future Enhancements

Category filtering (e.g., electronics, books)

Date-based search

SQLite or cloud storage support

Slack or email notifications









