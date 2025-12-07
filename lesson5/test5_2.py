import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator, PruningContentFilter

async def main():
    run_config = CrawlerRunConfig(
        markdown_generator = DefaultMarkdownGenerator(
            content_filter = PruningContentFilter(
                min_word_threshold = 50,
                threshold_type = 'fixed',
                threshold = 0.6
            ),
        ),
        excluded_tags = ['nav','footer','header','aside','form'],
        css_selector = 'article, .content, .post-content, entry-content, main'

    )

    async with AsyncWebCrawler() as crawler:
        url = 'https://blockcast.it/2025/07/21/bitcoins-dominance-slides-by-most-in-3-years-altcoin-season-imminent/'
        result = await crawler.arun(url = url)
        print(type(result))
        print(result.markdown)

if __name__ == '__main__':
    asyncio.run(main())
