import asyncio
from fastmcp import Client

client = Client("server.py")

async def main():
    async with client:
        print(await client.list_tools())
        #print(await mcp_client.call("get_weather", {"city": "New York"}))

asyncio.run(main())