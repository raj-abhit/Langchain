from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser)

#print(chain.invoke({'topic':'ai'}))

prompt2 = PromptTemplate(
    template = 'explain this joke: {response}',
    input_variables = ['response']
)

chain2 = RunnableSequence(prompt1, model, parser,prompt2, model, parser)

print(chain2.invoke({'topic':'ai'}))