"""Trends API quickstart - pytrends alternative. Get a free key at https://trendsapi.ai/#get-key"""
import os

import requests

res = requests.post(
    "https://api.trendsapi.ai/api",
    headers={"Authorization": f"Bearer {os.environ['TRENDSAPI_KEY']}"},
    json={
        "mode": "get_growth",
        "source": "google search",
        "keyword": "bitcoin",
        "percent_growth": ["3M", "12M"],
    },
    timeout=30,
)
res.raise_for_status()
print(res.json())
