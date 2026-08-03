# pytrends alternative - managed Google Trends API as JSON

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![API v1](https://img.shields.io/badge/API-v1-blue.svg)](https://trendsapi.ai) [![MCP compatible](https://img.shields.io/badge/MCP-compatible-blueviolet.svg)](https://modelcontextprotocol.io) [![Free tier](https://img.shields.io/badge/free%20tier-100%20req%2Fmo-orange.svg)](https://trendsapi.ai/#pricing)

> **The managed pytrends alternative: Google Trends data via a stable JSON API. No scraping, no 429 errors, no proxy rotation, no 2am broken pipelines. 15 keyword sources, 21 live trend feeds, 5 years of weekly history.**
>
> One endpoint. One API key. One normalized 0-100 trend score you can compare against 14 other platforms.

**Docs:** [https://trendsapi.ai/#quickstart](https://trendsapi.ai/#quickstart) · **llms.txt:** [https://trendsapi.ai/llms.txt](https://trendsapi.ai/llms.txt) · **Free API key (100 req/mo):** [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key)

---

## What a call looks like

```bash
curl -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "get_growth", "source": "google search", "keyword": "bitcoin", "percent_growth": ["3M", "12M"]}'
```

```json
{
  "keyword": "bitcoin",
  "source": "google search",
  "growth": { "3M": 41.8, "12M": 212.4 },
  "timestamp": "2026-08-03T12:00:00Z"
}
```

## Quickstart (60 seconds)

**1. Get a free API key** at [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key) - 100 requests/month, no credit card.

**2. Make your first call:**

```bash
curl -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "get_time_series", "source": "google search", "keyword": "bitcoin"}'
```

**Python:**

```python
import requests

res = requests.post(
    "https://api.trendsapi.ai/api",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={"mode": "get_growth", "source": "google search", "keyword": "bitcoin",
          "percent_growth": ["3M", "12M"]},
)
print(res.json())
```

**Node.js:**

```js
const res = await fetch("https://api.trendsapi.ai/api", {
  method: "POST",
  headers: {
    Authorization: "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ mode: "get_growth", source: "google search", keyword: "bitcoin",
                          percent_growth: ["3M", "12M"] }),
});
console.log(await res.json());
```

---

## The three modes

| Mode | What it returns | Needs a keyword? |
|---|---|---|
| `get_time_series` | Historical search interest as a normalized 0-100 series | yes |
| `get_growth` | Growth % over 3M / 6M / 12M / 5Y windows | yes |
| `get_top_trends` | Live trending feeds (21 of them) | no |

## Why teams switch

|  | pytrends (archived) | Trends API |
|---|---|---|
| 429 rate-limit errors | constant | never |
| Proxy rotation | often required | never |
| Breaks on Google changes | yes, regularly | no - managed infra |
| Platforms covered | 1 (Google only) | 15 sources + 21 feeds |
| Absolute growth windows | compute yourself | 3M/6M/12M/5Y built in |
| Maintenance status | archived | actively maintained |
| Free tier | free but blocked | 100 requests/month |

## Use cases

- **Migrate an existing pytrends pipeline** in an afternoon - one POST replaces the scraping stack
- **SEO research:** keyword interest over time without rate-limit babysitting
- **Market research:** demand signals across Google plus 14 other platforms in the same schema
- **Reporting:** scheduled trend pulls that do not break when Google changes a header

---

## Use it from your AI assistant (MCP)

The same API key powers the Trends API MCP server, so Claude, Cursor, VS Code, ChatGPT and any MCP-compatible client can query this data in natural language.

[**+ Add to Cursor (one click)**](cursor://anysphere.cursor-deeplink/mcp/install?name=trendsapi&config=eyJ1cmwiOiAiaHR0cHM6Ly9hcGkudHJlbmRzYXBpLmFpL21jcCIsICJoZWFkZXJzIjogeyJBdXRob3JpemF0aW9uIjogIkJlYXJlciBZT1VSX0FQSV9LRVkifX0=)

**Cursor / Windsurf / Cline** (`~/.cursor/mcp.json` or equivalent):

```json
{
  "mcpServers": {
    "trendsapi": {
      "url": "https://api.trendsapi.ai/mcp",
      "transport": "http",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**VS Code / GitHub Copilot** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "trendsapi": {
      "type": "http",
      "url": "https://api.trendsapi.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Claude Desktop** (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "trendsapi": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.trendsapi.ai/mcp", "--header", "Authorization:${AUTH_HEADER}"],
      "env": { "AUTH_HEADER": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Claude.ai (browser):** Settings -> Connectors -> Add custom connector -> `https://api.trendsapi.ai/mcp`

Then ask things like:

```
How did "creatine gummies" grow on TikTok vs Google over the last 12 months?
What is trending on YouTube right now?
```

---

## Every source on the same key

| Source | `source` value | What it measures |
|---|---|---|
| Google Search | `google search` | Search volume |
| Google Images | `google images` | Image search volume |
| Google News | `google news` | News search volume |
| Google Shopping | `google shopping` | Shopping search volume |
| YouTube | `youtube` | Search volume |
| TikTok | `tiktok` | Hashtag volume |
| Reddit | `reddit` | Subreddit subscribers |
| Amazon | `amazon` | Product search volume |
| Wikipedia | `wikipedia` | Page views |
| News volume | `news volume` | Article mention volume |
| News sentiment | `news sentiment` | Positive / negative score |
| App downloads | `app downloads` | Android downloads (AppBrain) |
| App rankings | `app rankings` | Android chart position |
| npm | `npm` | Weekly package downloads |
| Steam | `steam` | Concurrent players (monthly) |

### Live feeds (`get_top_trends`, no keyword needed)

| Feed | `type` value |
|---|---|
| Google Trends | `Google Trends` |
| Google News Top News | `Google News Top News` |
| TikTok Trending Hashtags | `TikTok Trending Hashtags` |
| TikTok Trending Searches | `TikTok Trending Searches` |
| TikTok Shop Hot Products | `TikTok Shop Hot Products` |
| YouTube Trending | `YouTube Trending` |
| X (Twitter) Trending | `X (Twitter) Trending` |
| Reddit Hot Posts | `Reddit Hot Posts` |
| Reddit World News | `Reddit World News` |
| Wikipedia Trending | `Wikipedia Trending` |
| Amazon Best Sellers Top Rated | `Amazon Best Sellers Top Rated` |
| Amazon Best Sellers by Category | `Amazon Best Sellers by Category` |
| App Store Top Free | `App Store Top Free` |
| App Store Top Paid | `App Store Top Paid` |
| Google Play | `Google Play` |
| Top Websites | `Top Websites` |
| Spotify Top Podcasts | `Spotify Top Podcasts` |
| Steam Most Played | `Steam Most Played` |
| GitHub Trending Repos | `GitHub Trending Repos` |
| IMDb MOVIEmeter | `IMDb MOVIEmeter` |
| Open Library Trending Books | `Open Library Trending Books` |

---

## FAQ

### Why was pytrends archived?

Google explicitly flags and blocks scrapers at the protocol level. Maintaining a scraping client became a losing game of whack-a-mole, so the maintainers archived the project. The demand for the data did not go away - only the reliable access did.

### Is Trends API a drop-in pytrends replacement?

Conceptually yes, mechanically different: instead of `pytrends.build_payload()` you make one POST with `source: "google search"` and your keyword. The response is a normalized time series with growth windows already computed. Most migrations are under an hour.

### What do I get that pytrends never offered?

Cross-platform coverage (TikTok, YouTube, Reddit, Amazon, npm, Steam and more in the same schema), built-in growth percentages, 21 live trending feeds, an MCP server for AI assistants, and infrastructure that does not break when Google changes something.

### Is there a free tier?

100 requests per month, no credit card. Enough to migrate and validate a pipeline before paying anything.

### Can I still use Python?

Yes. Plain `requests` works, and there is a first-party Python client in [trendsapi-py](https://github.com/trendsapi/trendsapi-py).

---

## Links

- **Docs & quickstart:** [https://trendsapi.ai/#quickstart](https://trendsapi.ai/#quickstart)
- **llms.txt (machine-readable API reference):** [https://trendsapi.ai/llms.txt](https://trendsapi.ai/llms.txt)
- **Pricing (free tier: 100 requests/month):** [https://trendsapi.ai/#pricing](https://trendsapi.ai/#pricing)
- **Get an API key:** [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key)

## License

MIT - see [LICENSE](LICENSE). Data is served by [Trends API](https://trendsapi.ai); usage of the API itself is subject to the plan limits on your key.
