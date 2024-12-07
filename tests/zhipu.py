import os
from openai import OpenAI 
 
def f(project):
    client = OpenAI(
        api_key=os.getenv("ZHIPUAI_API_KEY"),
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    ) 
    
    tools = [{
        "type": "web_search",
        "web_search": {
            "enable": True  # 启用网络搜索
        }
    }]

    response = client.chat.completions.create(
        model="glm-4",  
        messages=[
            {"role": "system", "content": "你是Github项目剖析专家，针对输入的Github项目url/名称\
                多维度多层次多视角详细介绍项目。发散思考产品如何商业化，以及产品的哲学意义。 \
                请用纯文本格式输出，不需要使用任何Markdown格式化，比如标题、加粗（** **）、斜体等。直接以普通文字表述即可。"},
            {"role": "user", "content": project},
        ],
        top_p=0.7,
        temperature=0.9,
        tools=tools
    ) 
    
    print(response .choices[0].message.content)

f('https://github.com/08183080/be-yourself')