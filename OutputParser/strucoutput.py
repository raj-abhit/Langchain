#from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

"""llm  =HuggingFaceEndpoint(repo_id = "google/gemma-2b-it",
                          task ="text-generation"
)

model = ChatHuggingFace(llm = llm)
"""


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template = 'write a detailed  report on {topic}',
    input_variables = ['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template = 'write a  summary on  the following text: {text}',
    input_variables = ['text']
)


prompt1 = template1.invoke({'topic':'blackholes'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

print(result1.content)
