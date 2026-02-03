from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="The sentiment of the feedback")
    
parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template= 'classify the feedback of the following {feedback} text into "positive" or "negative"\n{format_instruction}: ',
    input_variables= ['feedback'],
    partial_variables= {'format_instruction':parser2.get_format_instructions()}

)
classifier_chain = prompt1 | model | parser2

"""result = (classifier_chain.invoke({'feedback': 'this is a terrible smartphone'})).sentiment

print(result)"""

prompt2 = PromptTemplate(
    template= 'Based on the following feedback: {feedback}, generate a d response.',
    input_variables= ['feedback']
)
prompt3 = PromptTemplate(
    template= 'Based on the following feedback: {feedback}, generate a d response.',
    input_variables= ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive",  prompt2 | model | parser),
    (lambda x: x.sentiment == "negative",  prompt3 | model | parser),
    lambda x:"could not find sentiment"
)

chain = classifier_chain | branch_chain

result =  chain.invoke({'feedback': 'I hate the new design of your website! It is not user-friendly and visually troubling.'})

#print(result)
chain.get_graph().print_ascii()