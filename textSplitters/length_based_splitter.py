"""
    Here we already know the length/size of the chunks we are creating
"""

from langchain_core.documents import CharacterTextSplitter
from langchain_core.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()  # Here we have the the pdf loader we load the pdf doc.

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)