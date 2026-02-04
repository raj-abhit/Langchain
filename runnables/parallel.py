from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence,RunnableParallel
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template = 'generate a tweet about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

#chain1 = RunnableParallel([prompt1,model,parser])

prompt2 = PromptTemplate(
    template = 'generate a linkedin post about {topic}',     
    input_variables = ['topic']
)
#chain2 = RunnableParallel([prompt2,model,parser])

parallel_chain = RunnableParallel({'tweet':RunnableSequence(prompt1,model,parser),'linkedin':RunnableSequence(prompt2,model,parser)})

result = parallel_chain.invoke({'topic':'artificial intelligence'})
print(result)