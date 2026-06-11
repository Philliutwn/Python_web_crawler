"""
import asyncio, crawl4ai
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url = "https://www.nbcnews.com/business")
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())  

"""
"""
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig


async def main():
    browser_config = BrowserConfig()
    run_config = CrawlerRunConfig()
    async with AsyncWebCrawler(verbose=False) as crawler:
        result = await crawler.arun(url="https://www.example.com",)
        print(result.markdown)

if __name__=="__main__":
    asyncio.run(main())

"""
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    browser_config = BrowserConfig(
        browser_type="chromium",
        headless=True,
        verbose=True
    )

    run_config = CrawlerRunConfig(
        word_count_threshold=50,
        cache_mode=CacheMode.BYPASS
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url = "https://example.com", config = run_config)
        print(result.markdown)

if __name__=="__main__"  :
    asyncio.run(main())      