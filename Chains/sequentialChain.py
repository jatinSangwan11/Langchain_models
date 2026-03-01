"""
    topic -> LLM -> report -> LLM -> summary  --------- this is sequential Chain
 """

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1 = PromptTemplate(
    template='Make a report of 100 words on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the report in 5 lines : {report}',
    input_variables=['report']
)

parser = StrOutputParser()

model = ChatOpenAI(model='gpt-4')

chain = prompt1 | model | parser | prompt2 | model | parser

result1 = chain.invoke({'topic': 'Cricket'})

print(result1)

# also check the flow i.e the graph

print(chain.get_graph().print_ascii())


