from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()

# this chain below and this flow is called LCEL - langchain expression language
# and also this is the pipeline
chain = prompt | model | parser

result = chain.invoke({"topic": "cricket"})

print("Result:::", result)

# we can also print the chain and will be able to visualize it 

chain.get_graph().print_ascii()