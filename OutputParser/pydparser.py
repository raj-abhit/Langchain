from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(ge=18, description="The age of the person")
    city: str = Field(description="The city where the person lives")
    

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Give me the name ,age and city of a fictional person\n {place}person \n {format_instructions}',
    input_variables = ['place'],
    partial_variables = {'format_instructions':parser.get_format_instructions()}
)

"""prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result=parser.parse(result.content)"""

chain = template | model | parser
final_result = chain.invoke({'place':'indian'})
print(final_result)