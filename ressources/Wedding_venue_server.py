from dotenv import load_dotenv

load_dotenv()

from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from typing import Dict, Any
from requests import get


mcp = FastMCP("mcp_server")

tavily_client = TavilyClient()


# Tool for searching the web
@mcp.tool()
def search_web(query: str, search_rank: int, max_search: int) -> Dict[str, Any]:
    """Search the web for information. You will give only plain text character and avoid special charachters please."""

    if search_rank > max_search:
        return {"message": "Search limit reached. Please summarize your findings and provide your final answer."}
    try:
        return tavily_client.search(query)
    except Exception as e:
        return {"error": str(e)}

# Prompt template
@mcp.prompt()
def prompt():
    """Search the web for a wedding venue"""
    return """
    You are a expert wedding venue agent that find the best solutions of wedding venue. You will not ask follow up questions. Your answer based on price (good valur for money), capacity (highest) and good reviews (a high number).

    You can use the following tool to answer the coordinator questions:
    -> search_web: Search the web for information you need with the max number of search needed.

    You have only 10 search at your disposition, so count them and then summarize them.
    """

if __name__ == "__main__":
    mcp.run(transport="stdio")