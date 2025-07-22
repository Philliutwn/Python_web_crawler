import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
        async with AsyncWebCrawler() as crawler:
            # Run the crawler on a URL
            url = 'https://blockcast.it/2025/07/21/bitcoins-dominance-slides-by-most-in-3-years-altcoin-season-imminent/'
            result = await crawler.arun(url= url)
            print(type(result))  # Check the type of result
            # Print the result
            #print(result.markdown)
            print(result.markdown)

if __name__ == '__main__':
    asyncio.run(main())
# This code is an example of using AsyncWebCrawler to scrape a webpage asynchronously.
# It initializes the crawler, runs it on a specified URL, and prints the type and a portion of the result's markdown content.
# The AsyncWebCrawler is designed to handle web scraping tasks in an asynchronous manner, allowing for efficient handling of multiple requests without blocking the event loop.
# The code is structured to run within an asyncio event loop, which is necessary for asynchronous operations.
# The `AsyncWebCrawler` class is assumed to be part of the `crawl4ai` package, which is designed for web scraping tasks.
# The `arun` method is used to run the crawler asynchronously, and the result is expected to contain a `markdown` attribute that holds the scraped content in markdown format.                  