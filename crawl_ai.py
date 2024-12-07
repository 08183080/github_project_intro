import os
import json
import asyncio
from openai import OpenAI
# from crawl4ai.web_crawler import WebCrawler
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

async def extract_tech_content(url):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            extraction_strategy=LLMExtractionStrategy(
                provider="openai/deepseek-chat",
                api_token=os.getenv('DEEPSEEK_API_KEY'),
                instruction="提取项目介绍",
                base_url='https://api.deepseek.com'
            ),
            bypass_cache=True,
        )
    return result.extracted_content

def get_project_intros(project):
    client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是Github项目剖析专家，针对输入的Github项目的结构化数据介绍\
             然后写篇中文文章多维度多层次多视角详细介绍项目。发散思考产品如何商业化，以及产品的哲学意义。 \
             请用纯文本格式输出，不需要使用任何Markdown格式化，比如标题、加粗（** **）、斜体等。直接以普通文字表述即可。"},
            {"role": "user", "content": project},
        ],
        stream=False
    )
    return response.choices[0].message.content

def get_project_intro(project):
    client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是Github项目剖析专家，针对输入的Github项目url/名称，\
             多维度多层次多视角详细介绍项目。发散思考产品如何商业化，以及产品的哲学意义。 \
             请用纯文本格式输出，不需要使用任何Markdown格式化，比如标题、加粗（** **）、斜体等。直接以普通文字表述即可。"},
            {"role": "user", "content": project},
        ],
        stream=False
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    url = "https://github.com/08183080/images_download"
    project = asyncio.run(extract_tech_content(url))
    # project = extract_content(url)
    if project == '' or len(project) < 20:
        ans = get_project_intro(url)
    else:
        ans = get_project_intros(project)
    print(ans)