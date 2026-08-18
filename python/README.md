# pytrends alternative

Managed Google Trends client for Python. Drop-in mindset for archived pytrends: history, growth, and 30+ other sources via the Trends API.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/pytrends-alternative.svg)](https://pypi.org/project/pytrends-alternative/)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

JS: [`pytrends-alternative`](https://www.npmjs.com/package/pytrends-alternative).

## Install

```bash
pip install pytrends-alternative
```

```python
from pytrends_alternative import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series("electric vehicle")
growth = client.get_growth("electric vehicle", percent_growth=["12M"])
hot = client.get_live(limit=10)
```

Keyword helpers default to `source: "google search"`. Override `source=` for any other platform. Official full client: [`trendsapi`](https://pypi.org/project/trendsapi/).

## Mapping

| pytrends | Here |
|---|---|
| `TrendReq(...)` + `build_payload(...)` | Not needed. One client call |
| `interest_over_time()` | `get_time_series("term")` |
| DataFrame `pct_change` | `get_growth("term", percent_growth=["3M","12M"])` |
| `trending_searches()` | `get_live()` or `get_top_trends(type="Google Trends")` |
| `interest_by_region()` | **No equivalent** |
| `related_queries()` / `related_topics()` | **No equivalent** |
| `proxies=`, cookies, User-Agent | Remove |

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: google search` with `get_time_series` or `get_growth` |
| Keyword | Any phrase |
| Live `type` | Google Trends |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"google search","keyword":"electric vehicle"}'
```

One keyword per request. Five terms in `kw_list` become five calls.

404 means no series for that spelling. Do not retry 404s.

Indexes will not match an old pytrends CSV cell-for-cell. Compare shape and direction, not exact 0-100 values.

Site: [https://trendsapi.ai/trends/pytrends-alternative](https://trendsapi.ai/trends/pytrends-alternative). GitHub: [trendsapi-ai/pytrends-alternative](https://github.com/trendsapi-ai/pytrends-alternative).

## License

MIT. See [LICENSE](LICENSE).
