# ...existing code...
import os
import logging
from pathlib import Path

import gradio as gr

# load .env from the same folder as this file
try:
    from dotenv import load_dotenv

    env_path = Path(__file__).resolve().parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
except Exception:
    # If python-dotenv is not installed, env vars may still be set in the environment
    pass

# Try to import Tavily and its specific error so we handle missing-key cleanly
try:
    from tavily import TavilyClient
    from tavily.errors import MissingAPIKeyError
except Exception:
    TavilyClient = None
    MissingAPIKeyError = Exception  # fallback

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Read Tavily API key from environment (now loaded from .env if present)
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Optionally use a mock mode for local testing (set MOCK_TAVILY=1 in .env)
USE_MOCK = os.environ.get("MOCK_TAVILY", "").lower() in ("1", "true", "yes")

# Initialize Tavily client only when we have a key and the package is importable
client = None
if TavilyClient is None:
    logger.warning("tavily package not available. Install it to enable real searches.")
elif TAVILY_API_KEY:
    try:
        client = TavilyClient(api_key=TAVILY_API_KEY)
        logger.info("Initialized TavilyClient from TAVILY_API_KEY.")
    except MissingAPIKeyError:
        logger.exception("Tavily reported missing API key at initialization.")
        client = None
    except Exception:
        logger.exception("Failed to initialize TavilyClient.")
        client = None
else:
    logger.info("TAVILY_API_KEY not found. Tavily client will not be initialized. "
                "Set TAVILY_API_KEY in .env or the environment to enable real searches.")

def _perform_search(query: str, search_depth: str = "basic", max_results: int = 5):
    """Call Tavily or return mock/error info."""
    if client is None:
        if USE_MOCK:
            logger.info("MOCK_TAVILY enabled — returning fake results for query: %s", query)
            return {
                "results": [
                    {"title": "Mock result", "content": f"Mock content for '{query}'", "url": "http://example.com"}
                ],
                "answer": "Mocked summary of results.",
            }
        msg = "Tavily client not initialized. Set TAVILY_API_KEY or enable MOCK_TAVILY=1 in .env"
        logger.error(msg)
        return {"error": msg}

    try:
        response = client.search(query=query, search_depth=search_depth, max_results=max_results)
        if not isinstance(response, dict):
            return {"results": [], "raw_response": response}
        return response
    except MissingAPIKeyError:
        msg = "Tavily reported missing API key when calling search."
        logger.exception(msg)
        return {"error": msg}
    except Exception as e:
        logger.exception("Tavily search failed for query: %s", query)
        return {"error": str(e)}


def get_city_weather_info(city_name: str):
    query = f"current weather in {city_name} temperature humidity conditions"
    resp = _perform_search(query, search_depth="basic", max_results=5)
    if "error" in resp:
        return {"city": city_name, "error": resp["error"], "search_query": query}

    weather_info = {"city": city_name, "search_query": query, "results": []}
    for result in resp.get("results", []):
        weather_info["results"].append(
            {"title": result.get("title", ""), "content": result.get("content", ""), "url": result.get("url", "")}
        )
    if "answer" in resp:
        weather_info["summary"] = resp["answer"]
    if "raw_response" in resp:
        weather_info["raw_response"] = resp["raw_response"]
    return weather_info


def get_city_news(city_name: str):
    query = f"Top 5 latest news articles about {city_name}, including major events, politics, economy, and local updates."
    resp = _perform_search(query, search_depth="advanced", max_results=5)
    if "error" in resp:
        return {"city": city_name, "error": resp["error"], "search_query": query}

    news_info = {"city": city_name, "search_query": query, "articles": []}
    for result in resp.get("results", []):
        news_info["articles"].append(
            {"title": result.get("title", ""), "content": result.get("content", ""), "url": result.get("url", "")}
        )
    if "answer" in resp:
        news_info["summary"] = resp["answer"]
    if "raw_response" in resp:
        news_info["raw_response"] = resp["raw_response"]
    return news_info


# Create Gradio interfaces
weather_demo = gr.Interface(
    fn=get_city_weather_info,
    inputs=gr.Textbox(label="Enter City Name", placeholder="e.g., New York"),
    outputs=gr.JSON(label="Weather Information"),
    description="Get current weather details for a city.",
)

news_demo = gr.Interface(
    fn=get_city_news,
    inputs=gr.Textbox(label="Enter City Name", placeholder="e.g., London"),
    outputs=gr.JSON(label="News Articles"),
    description="Get the latest news articles for a city.",
)

demo = gr.TabbedInterface([weather_demo, news_demo], ["Weather", "News"], title="City Information Hub")

# ...existing code...
if __name__ == "__main__":
    # On HuggingFace Spaces, do not use MCP and keep public sharing off.
    # Use environment variables to control behavior if needed.
    HF_SPACE = os.environ.get("HF_SPACE", "").lower() in ("1", "true", "yes")
    demo.launch(share=False, mcp_server=True, debug=not HF_SPACE)
# ...existing code...