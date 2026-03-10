from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from dotenv import load_dotenv

load_dotenv()

model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key=DEEPSEEK_API_KEY),
)
agent = Agent(model)
...