import requests
import os
import re
from openai import OpenAI
from tavily import TavilyClient
from dotenv import load_dotenv

class OpenAICompatibleClient:
    """
    一个用于调用任何兼容OpenAI接口的LLM服务的客户端。
    """
    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system_prompt: str) -> str:
        """调用LLM API来生成回应。"""
        print("正在调用大语言模型...")
        try:
            messages = [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=False
            )
            answer = response.choices[0].message.content
            print("大语言模型响应成功。")
            return answer
        except Exception as e:
            print(f"调用LLM API时发生错误: {e}")
            return "错误：调用语言模型服务时出错。"

class TravelAssistant:
    """
    智能旅行助手类
    """
    def __init__(self):
        self.llm = OpenAICompatibleClient(
            model=MODEL_ID,
            api_key=API_KEY,
            base_url=BASE_URL
        )
        self.prompt_history = []
    
    def reset(self):
        """重置对话历史"""
        self.prompt_history = []
    
    def add_user_message(self, message: str):
        """添加用户消息到历史"""
        self.prompt_history.append(f"用户请求: {message}")
    
    def add_assistant_message(self, message: str):
        """添加助手消息到历史"""
        self.prompt_history.append(message)
    
    def add_observation(self, observation: str):
        """添加观察结果到历史"""
        self.prompt_history.append(f"Observation: {observation}")
print("✅ 智能助手类定义完成!")