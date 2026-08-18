# pytrends alternative

[pytrends](https://pypi.org/project/pytrends/) is archived. Google blocks the endpoints it scraped. This package maps that workflow onto [Trends API](https://trendsapi.ai): **three modes**, not ten.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![npm](https://img.shields.io/npm/v/pytrends-alternative.svg)](https://www.npmjs.com/package/pytrends-alternative)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi). General Google JSON: [google-trends-api](https://github.com/trendsapi-ai/google-trends-api).

## Install

```bash
npm install pytrends-alternative
```

```ts
import { TrendsAPI } from "pytrends-alternative";

const client = new TrendsAPI({ apiKey: process.env.TRENDSAPI_KEY });
const series = await client.getTimeSeries("electric vehicle");
const growth = await client.getGrowth("electric vehicle", {
  percent_growth: ["3M", "6M", "12M"],
});
const hot = await client.getTopTrends({ type: "Google Trends", limit: 20 });
```

Keyword helpers default to `source: "google search"`. Python: `pip install trendsapi`. Official full JS client: [`trendsapi`](https://www.npmjs.com/package/trendsapi).

## Mapping

| pytrends | Trends API |
|---|---|
| `TrendReq(...)` + `build_payload(...)` | Not needed. One client call |
| `interest_over_time()` | `getTimeSeries("term")` or `mode: get_time_series`, `source: google search` |
| DataFrame `pct_change` | `getGrowth("term", { percent_growth: ["3M","12M"] })` |
| `trending_searches()` | `getTopTrends({ type: "Google Trends" })` |
| `interest_by_region()` | **No equivalent** |
| `related_queries()` / `related_topics()` | **No equivalent** |
| `proxies=`, cookies, User-Agent | Remove |

One keyword per request. Five terms in `kw_list` become five calls.

404 means no series for that spelling (same role as an empty pytrends frame). Do not retry 404s.

Indexes will not match an old pytrends CSV cell-for-cell. Compare shape and direction, not exact 0-100 values.

Site: [trendsapi.ai/trends/pytrends-alternative](https://trendsapi.ai/trends/pytrends-alternative).

## License

MIT. See [LICENSE](LICENSE).
