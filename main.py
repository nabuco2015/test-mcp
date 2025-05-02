import logging
from fastmcp import FastMCP

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Starting application with DEBUG logging enabled")

mcp = FastMCP("weather")

@mcp.tool("get_weather", "This tool gets the current temperature in a city.")
async def get_weather(city_name: str) -> int:
    """
    This tool gets the current temperature in a city.

    Args:
        city_name: str

    Returns:
        int: The temperature in the city
    """
    import random
    return random.randint(14, 25)

__all__ = ["mcp"]

if __name__ == "__main__":
    # Explicitly set host to 0.0.0.0 to listen on all interfaces
    mcp.run(transport="sse", host="0.0.0.0")
