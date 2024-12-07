import os
import json
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

async def extract_tech_content():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://github.com/08183080/images_download",
            extraction_strategy=LLMExtractionStrategy(
                provider="openai/deepseek-chat",
                api_token=os.getenv('DEEPSEEK_API_KEY'),
                instruction="提取项目介绍",
                base_url='https://api.deepseek.com'
            ),
            bypass_cache=True,
        )
    print(result.extracted_content)
    # tech_content = json.loads(result.extracted_content)
    # print(tech_content)
    # print(f"Number of tech-related items extracted: {len(tech_content)}")

    # with open("./tech_content.json", "w", encoding="utf-8") as f:
    #     json.dump(tech_content, f, indent=2)

asyncio.run(extract_tech_content())