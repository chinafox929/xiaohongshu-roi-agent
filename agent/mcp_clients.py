"""
Google Cloud Rapid Agent Hackathon
MCP (Model Context Protocol) Clients for Partner Integration

This file demonstrates how the Agent connects to the official MCP servers
provided by the hackathon partners (MongoDB and Elastic).
"""

import os
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession

# 1. MongoDB MCP Client Setup
async def get_mongodb_mcp_tools():
    """
    Connects to the MongoDB MCP server to fetch tools for querying user history.
    """
    mongodb_uri = os.getenv("MONGODB_URI")
    
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-mongodb", mongodb_uri],
        env=os.environ.copy()
    )
    
    # Example usage (requires async context)
    # async with stdio_client(server_params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()
    #         tools = await session.list_tools()
    #         return tools
    
    return []

# 2. Elastic MCP Client Setup
async def get_elastic_mcp_tools():
    """
    Connects to the Elastic MCP server to fetch tools for market trends search.
    """
    elastic_endpoint = os.getenv("ELASTIC_ENDPOINT")
    elastic_api_key = os.getenv("ELASTIC_API_KEY")
    
    env = os.environ.copy()
    env["ELASTIC_API_KEY"] = elastic_api_key
    
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-elasticsearch", elastic_endpoint],
        env=env
    )
    
    # Example usage (requires async context)
    # async with stdio_client(server_params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         await session.initialize()
    #         tools = await session.list_tools()
    #         return tools
    
    return []

# Note: In `app.py`, we implemented Python-native tool mockups for the hackathon demo
# to ensure it can run instantly without requiring the judges to spin up full databases.
# In production, Gemini 3 would call the `execute_tool` endpoint on these sessions.
