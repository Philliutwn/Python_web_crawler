import asyncio
from crawl4ai import(AsyncWebCrawler,
                     CrawlerRunConfig,
                     DefaultMarkdownGenerator,
                     PruningContentFilter)

async def main():
    #建立一個AsyncWebCrawler的實體
    run_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.6,
                threshold_type= 'fixed',
                min_word_threshold=50
            ),
        ),
        # 移除不必要的元素
        excluded_tags = ['nav','footer','header','aside','form'],
        # 專門針對文章內容的CSS選擇器(可選)
        css_selector = 'article, .content, .post-content, entry-content, main'
    )
    
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