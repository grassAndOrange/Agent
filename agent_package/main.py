import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from dotenv import load_dotenv
import tools
load_dotenv()

model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key= os.getenv("DEEPSEEK_API_KEY")),
)
agent = Agent(model
              ,system_prompt="You are a helpful assistant that can read, list, and rename files in the './test' directory. Use the provided tools to perform these actions when requested."
              ,tools=[tools.read_file, tools.list_files, tools.rename_file, tools.create_file])
def main():
    print("Hello! I'm a Pydantic AI agent using DeepSeek. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = agent.run_sync(user_input)
        print(f"Agent: {response.output}")

if __name__ == '__main__':
    main()