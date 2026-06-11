# Basic crawling from crawl4ai website "Basic crawling"

import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()
    run_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config = browser_config) as crawler:
        result = await crawler.arun(url = "https://example.com", config = run_config)
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
    