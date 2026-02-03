from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template = 'write a detailed  report on {topic}',
    input_variables = ['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template = 'write a 5 line summary on  the following text: {text}',
    input_variables = ['text']
)


parser = StrOutputParser()

chain = template1 | model | template2 | model | parser

result=chain.invoke({'topic':'blackholes'})

print(result)