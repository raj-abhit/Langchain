from langchain_community.document_loaders.text import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()
prompt = PromptTemplate(
    template = 'write a summary for this topic: \n{topic}',
    input_variables = ['topic']
)
    

loader = TextLoader("landmark_cases.txt",encoding = "utf-8")
 
docs = loader.load()

"""print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
"""
chain = prompt | model | parser

result = chain.invoke({'topic':docs[0].page_content})
print(result)