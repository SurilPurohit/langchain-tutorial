from langchain_xai import ChatXAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatXAI(model='grok-3-beta') 

result = llm.invoke("What is the capital of India?")
print(result.content)