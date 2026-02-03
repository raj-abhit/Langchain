from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="llama-3.1-8b-instant")

llm  =HuggingFaceEndpoint(repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                          task ="text-generation"
)
model2 = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template= 'Generate a short and simple report on {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template= 'Generate a small 5 point summary on the following topic: {topic}\n',
    input_variables= ['topic']
)

prompt3 = PromptTemplate(
    template= 'merge the provided report and summary in a single document\n report ->{report}\n summary ->{summary}',
    input_variables= ['report', 'summary']
)

parser = StrOutputParser()

parallel = RunnableParallel({
    'report': prompt1 | model1 | parser,
    'summary': prompt2 | model1 | parser
})
    
merge_chain = prompt3 | model1 | parser

chain = parallel | merge_chain
    
result = chain.invoke({'topic':'blackholes'})
#print(result)
chain.get_graph().print_ascii()