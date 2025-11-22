import os
from serpapi import GoogleSearch
from dotenv import load_dotenv  # 👈 add this

# Load .env file
load_dotenv()

# Now fetch your API key
SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # set this in your environment

def research_query(query, site_filter="site:gov.in"):
    params = {
        "engine": "google",
        "q": f"{query} {site_filter}",
        "api_key": SERPAPI_KEY,
        "num": 3
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic = results.get("organic_results", [])
    snippets = []
    for item in organic:
        title = item.get("title")
        link = item.get("link")
        snippet = item.get("snippet")
        snippets.append({"title": title, "link": link, "snippet": snippet})
    return snippets
