import os
import requests
from langchain_tavily import TavilySearch


class SerperPlaceSearchTool:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY not found")

        self.base_url = "https://google.serper.dev/search"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def _search(self, query: str) -> dict:
        payload = {"q": query}
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    def google_search_attractions(self, place: str) -> dict:
        return self._search(f"top attractions in and around {place}")

    def google_search_restaurants(self, place: str) -> dict:
        return self._search(f"top 10 restaurants and eateries in {place}")

    def google_search_activity(self, place: str) -> dict:
        return self._search(f"popular activities in and around {place}")

    def google_search_transportation(self, place: str) -> dict:
        return self._search(f"modes of transportation available in {place}")


# -------------------------------
# Tavily stays as-is (good choice)
# -------------------------------

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> str | dict:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractions in and around {place}"})
        return result.get("answer", result)

    def tavily_search_restaurants(self, place: str) -> str | dict:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top 10 restaurants in {place}"})
        return result.get("answer", result)

    def tavily_search_activity(self, place: str) -> str | dict:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        return result.get("answer", result)

    def tavily_search_transportation(self, place: str) -> str | dict:
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"transportation options in {place}"})
        return result.get("answer", result)
