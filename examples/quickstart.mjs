import { TrendsAPI } from "pytrends-alternative";

const client = new TrendsAPI({ apiKey: process.env.TRENDSAPI_KEY });
const series = await client.getTimeSeries("electric vehicle");
console.log(series.at(-1));
