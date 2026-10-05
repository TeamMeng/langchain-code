import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

assert os.getenv("DEEPSEEK_API_KEY"), "请在 .env 里配置 DEEPSEEK_API_KEY"

model = init_chat_model("deepseek-flash")

res = model.invoke("Hello")

print(res)
