# pytrends alternative

Managed Google Trends client for Python. Drop-in mindset for archived pytrends: history, growth, and 30+ other sources via the Trends API.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/pytrends-alternative.svg)](https://pypi.org/project/pytrends-alternative/)
[![Python](https://img.shields.io/badge/python-3.9%2B-yellow.svg)](https://trendsapi.ai)
[![npm](https://img.shields.io/npm/v/pytrends-alternative.svg)](https://www.npmjs.com/package/pytrends-alternative)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). HTTP contract and every source: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Authentication

```bash
pip install pytrends-alternative
export TRENDSAPI_KEY=your_key
```

Python 3.9+. Same key as the HTTP API.

```python
from pytrends_alternative import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")
```

Keyword helpers default to `source: "google search"`. Pass `source=` to hit any other platform with the same client. Official full client (every source, no preset): [`trendsapi`](https://pypi.org/project/trendsapi/).

## Methods

| Method | REST `mode` | Returns |
|---|---|---|
| `get_time_series(keyword, source=, data_mode=)` | `get_time_series` | `list[TrendsDataPoint]` |
| `get_growth(keyword, percent_growth=, source=, data_mode=)` | `get_growth` | `GetGrowthResponse` |
| `get_live(limit=, offset=, category=)` | `get_top_trends` | `GetTopTrendsResponse` |
| `get_top_trends(type=, ...)` | `get_top_trends` | `GetTopTrendsResponse` |

`source` is lowercase (`google search`). `type` is exact (`Google Trends`). Mixing them is a 400.

```python
from pytrends_alternative import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")

series = client.get_time_series("electric vehicle")
print(series[-1].date, series[-1].value)

growth = client.get_growth("electric vehicle", percent_growth=["3M", "12M"])
print(growth.results[0].growth, growth.results[0].direction)

hot = client.get_live(limit=10)
print(hot.data)                         # [[1, "..."], ...]
```

## get_time_series

```python
points = client.get_time_series("electric vehicle")
```

Each point:

| Field | Always | Meaning |
|---|---|---|
| `date` | yes | `YYYY-MM-DD` |
| `value` | yes | 0-100 index for this series |
| `keyword` | yes | Echo |
| `volume` | no | Absolute volume when available |
| `source` or `datatype` | no | Pipeline label |

Python returns `list[TrendsDataPoint]`. Use `.date` and `.value`, not `["date"]`.
JS returns the same fields as object properties.

## get_growth

```python
g = client.get_growth("electric vehicle", percent_growth=["12M", "3M", "YTD"])
print(g.results[0].growth, g.results[0].direction)
```

`percent_growth` default: `["12M"]`. Presets: `7D` `14D` `30D` `1M` `2M` `3M` `6M` `9M` `12M`/`1Y` `18M` `24M`/`2Y` `36M`/`3Y` `48M` `60M`/`5Y` `MTD` `QTD` `YTD`. Custom: `{"name": "Launch", "recent": "2024-06-01", "baseline": "2024-01-01"}`.

| Field | Meaning |
|---|---|
| `search_term` | Keyword |
| `data_source` | Source |
| `results` | One object per window (`period`, `growth`, `direction`, dates, values) |
| `metadata` | Counts / success flag |

Several windows still count as one request. Python: `growth.results[0].growth`. JS: `growth.results[0].growth`.


## get_live

```python
hot = client.get_live(limit=10)
```

| Field | Meaning |
|---|---|
| `as_of_ts` | Snapshot time |
| `type` | Feed name |
| `limit`, `offset`, `count` | Pagination |
| `data` | `[rank, label]` rows |

Python: `hot.data`. JS: `hot.data`. Optional `offset=` and `category=` (`Amazon Best Sellers by Category`, `Top Websites` only).


## Async

```python
import asyncio
from pytrends_alternative import AsyncTrendsAPI

async def main():
    c = AsyncTrendsAPI()
    return await asyncio.gather(
        c.get_time_series("electric vehicle"),
    )

asyncio.run(main())
```

Each 200 is one billed request.

## Pandas

```python
from dataclasses import asdict
import pandas as pd
from pytrends_alternative import TrendsAPI

df = pd.DataFrame(asdict(p) for p in TrendsAPI().get_time_series("electric vehicle"))
df["date"] = pd.to_datetime(df["date"])
print(df.set_index("date")["value"].resample("ME").mean().tail())
```

## JavaScript / TypeScript

```bash
npm install pytrends-alternative
```

Node 18+, Deno, Bun, Workers. Same API key. Field tables above apply.

### Methods

| Method | REST `mode` | Returns |
|---|---|---|
| `getTimeSeries(keyword, { source, data_mode })` | `get_time_series` | weekly points |
| `getGrowth(keyword, { percent_growth, source, data_mode })` | `get_growth` | growth object |
| `getLive({ limit, offset, category })` | `get_top_trends` | live feed |
| `getTopTrends({ type, ... })` | `get_top_trends` | live feed |

```ts
import { TrendsAPI } from "pytrends-alternative";

const client = new TrendsAPI({ apiKey: process.env.TRENDSAPI_KEY! });
const series = await client.getTimeSeries("electric vehicle");
console.log(series.at(-1)?.date, series.at(-1)?.value);

const growth = await client.getGrowth("electric vehicle", {
  percent_growth: ["3M", "12M"],
});
console.log(growth.results[0].growth, growth.results[0].direction);

const live = await client.getLive({ limit: 10 });
console.log(live.data);                 // [[1, "..."], ...]
```

## Mapping from pytrends

| pytrends | Here |
|---|---|
| `TrendReq(...)` + `build_payload(...)` | Not needed. One client call |
| `interest_over_time()` | `get_time_series("term")` |
| DataFrame `pct_change` | `get_growth("term", percent_growth=["3M", "12M"])` |
| `trending_searches()` | `get_live()` or `get_top_trends(type="Google Trends")` |
| `interest_by_region()` | **No equivalent** |
| `related_queries()` / `related_topics()` | **No equivalent** |
| `proxies=`, cookies, User-Agent | Remove |

One keyword per request. Five terms in an old `kw_list` become five calls.

## Call (curl)

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

## Source notes

- One keyword per request. Five terms in `kw_list` become five calls.
- 404 means no series for that spelling. Do not retry 404s.
- Indexes will not match an old pytrends CSV cell-for-cell. Compare shape and direction, not exact 0-100 values.

## Errors

| HTTP | Client |
|---|---|
| 200 | Parsed payload. Python dataclasses / JS typed objects |
| 400 | Raises. Fix `source` or `type` spelling |
| 401 | Raises. Check `TRENDSAPI_KEY` |
| 404 | Raises. No series for that keyword. Do not retry |
| 429 | Raises. Quota |
| 5xx | Client retries, then raises |

The HTTP `body` field is a JSON string. SDKs decode it. Raw curl must parse `body` a second time.

Site: [https://trendsapi.ai/trends/pytrends-alternative](https://trendsapi.ai/trends/pytrends-alternative).

## License

MIT. See [LICENSE](LICENSE).
