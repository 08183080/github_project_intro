from zhipuai import ZhipuAI
from datetime import datetime
import os

# 初始化 ZhipuAI 客户端
client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY"))

# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")

# 设置工具（启用网络搜索）
tools = [{
    "type": "web_search",
    "web_search": {
        "enable": True  # 启用网络搜索
    }
}]

# 系统提示模板，包含时间信息
system_prompt = f"""你是一个具备网络访问能力的智能助手，在适当情况下，优先使用网络信息（参考信息）来回答，
以确保用户得到最新、准确的帮助。当前日期是 {current_date}。"""

# 用户输入的问题
user_input = "2024年美国大选的结果"

# 构建动态用户问题提示
user_question = f"参考最新消息给出对用户输入的回答: {user_input}"

# 构建消息
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_question}
]

# 生成响应
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=messages,
    tools=tools
)

# 输出结果
print(response.choices[0].message)
