from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_groq import ChatGroq

loader = PyPDFLoader("bns.pdf")

docs =loader.load()

print(len(docs),type(docs))

print(docs[0].page_content[:100])  # Print the first 100 characters of the first page content
print(docs[0].metadata)  # Print metadata of the first page

