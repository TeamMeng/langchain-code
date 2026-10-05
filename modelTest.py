import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

assert os.getenv("DEEPSEEK_API_KEY"), "请在 .env 里配置 DEEPSEEK_API_KEY"

model = init_chat_model("deepseek-flash")

conversation = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("I'm Team Meng"),
    AIMessage("Hello, Team Meng"),
    HumanMessage("Who am i?"),
]

res = model.stream(conversation)

for chunk in res:
    print(chunk.content)
