from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()    # env variables loaded 

model = ChatOpenAI(model="gpt-4", temperature=0.4, max_completion_tokens=10)

result = model.invoke("what is the capital of India?")

print("Result:::", result.content)

# NOTES
"""
what is temperature? 
--> it is the randomess in the AI LLM chatModel response we want the lower the value more deterministic the result and higher means more creativity

"""