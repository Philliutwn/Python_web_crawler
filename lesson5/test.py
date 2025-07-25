import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
    
    url = 'https://www.bnext.com.tw/article/83931/2025-virtual-power-plant--vpp'
    schema = {
        "name":"範例項目",
        "baseSelector":"[data-desc='內文']",
        "fields":[
            {
                "name":"標題",
                "selector":"h1",
                "type":"text"
            },
            {
                "name":"時間",
                "selector":"span.time",
                "type":"text"
                
            }
        ]
    }

    #CrawlerRunConfig實體
    run_config = CrawlerRunConfig(
        cache_mode = CacheMode.BYPASS,
        extraction_strategy = JsonCssExtractionStrategy(schema=schema)
    )    
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(
            url = url,
            config = run_config
        )

        print(type(result.extracted_content))  # Check the type of result
        # Print the result
        #print(result.markdown)
        print(result.extracted_content)

if __name__ == '__main__':
    asyncio.run(main())