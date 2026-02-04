from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableBranch

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a detail report about  {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'write a summary about  {text}',
    input_variables = ['text']
)

#report_chain = RunnableSequence(prompt1, model, parser)
report_chain = prompt1 | model | parser

"""branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)"""

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, prompt2 | model | parser),  #RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

result = final_chain.invoke({'topic':'russia ukraine war'})

print(result)


    