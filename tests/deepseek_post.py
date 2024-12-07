import os
from openai import OpenAI


def get_project(path):
    with open(path, 'r') as f:
        return f.read()
    
def get_project_intro(project):
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

if __name__ == '__main__':
    print(get_project_intro(get_project('./tech_content.json')))
    # print(get_project_intro("https://github.com/openai/openai-cookbook"))
    # print(get_project_intro("https://github.com/microsoft/mu_feature_ipmi"))
    # print(get_project_intro('https://github.com/jubalh/awesome-os'))
    # print(get_project_intro('https://github.com/08183080/be-yourself'))
    # print(get_project_intro('https://github.com/FoundationVision/VAR'))