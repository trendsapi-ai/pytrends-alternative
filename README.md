# pytrends alternative

[pytrends](https://pypi.org/project/pytrends/) is archived. Google blocks the endpoints it scraped. This guide maps pytrends methods onto [Trends API](https://trendsapi.ai), which has **three modes**, not ten.

General Google JSON (not a migration): [google-trends-api](https://github.com/trendsapi-ai/google-trends-api). Contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi). Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Guide](https://img.shields.io/badge/guide-pytrends%20to%20JSON-blue.svg)](https://trendsapi.ai/trends/pytrends-alternative)
[![npm](https://img.shields.io/npm/v/pytrends-alternative.svg)](https://www.npmjs.com/package/pytrends-alternative)

```bash
npm install pytrends-alternative
```

## Mapping

| pytrends | Trends API |
|---|---|
| `TrendReq(...)` + `build_payload(...)` | Not needed. One POST (or one SDK call) |
| `interest_over_time()` | `mode: get_time_series`, `source: google search` |
| DataFrame `pct_change` | `mode: get_growth`, `percent_growth: ["3M","12M"]` |
| `trending_searches()` | `mode: get_top_trends`, `type: Google Trends` |
| `interest_by_region()` | **No equivalent** |
| `related_queries()` / `related_topics()` | **No equivalent** |
| `proxies=`, cookies, User-Agent | Remove |

## After

```python
from trendsapi import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
rows = client.get_time_series(source="google search", keyword="electric vehicle")
growth = client.get_growth(
    source="google search",
    keyword="electric vehicle",
    percent_growth=["3M", "6M", "12M"],
)
hot = client.get_top_trends(type="Google Trends", limit=20)
```

Raw HTTP (parse `body` twice): [hub, Raw HTTP](https://github.com/trendsapi-ai/trendsapi#raw-http).

One keyword per request. Five terms in `kw_list` become five calls.

404 means no series for that spelling (same role as an empty pytrends frame). Do not retry 404s.

Indexes will not match an old pytrends CSV cell-for-cell. Compare shape and direction, not exact 0-100 values.

## License

MIT. See [LICENSE](LICENSE).
