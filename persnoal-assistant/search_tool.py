from serpapi import GoogleSearch
from secret import SERPAPI_API_KEY

def google_search(query):
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google",
        "num": 1,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [{}])[0].get("link", "No result found.")
