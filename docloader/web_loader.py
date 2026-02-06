from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Set USER_AGENT BEFORE loading dotenv
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

load_dotenv()

parser = StrOutputParser()
url = 'https://en.wikipedia.org/wiki/2026_Winter_Olympics'
loader = WebBaseLoader(url)
model = ChatGroq(model="llama-3.1-8b-instant")
docs = loader.load()

prompt = PromptTemplate(
    template = 'Answer the following question \n{question}from the following text \n{text}',
    input_variables = ['question','text']
)

# Truncate content to first 2000 characters to avoid token limit
truncated_content = docs[0].page_content[:2000]

chain = prompt | model | parser

print(chain.invoke({'question':'when is the olympics?','text':truncated_content}))