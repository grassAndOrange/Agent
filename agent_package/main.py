import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from dotenv import load_dotenv
from . import tools
load_dotenv()

model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key= os.getenv("DEEPSEEK_API_KEY")),
)
agent = Agent(model,system_prompt="You are a helpful assistant that can read, list, and rename files in the './test' directory. Use the provided tools to perform these actions when requested.")
def main():
    print("Hello! I'm a Pydantic AI agent using DeepSeek. How can I assist you today?")

if __name__ == '__main__':
    main()