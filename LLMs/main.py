from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

response = llm.invoke(
    "what is the capital of England?"
)

print("This is the reply from the LLM prompt:::", response)


# the above code is not used anymore...