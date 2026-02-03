
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import StructuredOutputParser#no longer exist replaced by PydanticOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")


schema = [
    ResponseSchema(name="fact1",description="fact 1 about the topic"),
    ResponseSchema(name="fact2",description="fact 2 about the topic"),
    
    ResponseSchema(name="fact3",description="fact 3 about the topic")
    
]
parser = StructuredOutputParser.from_response_schemas(schema)
 
template  = PromptTemplate(
    template = 'Give me 3 facts about  {topic} \n {format_instructions}',
    input_variables = ['topic'],    
    partial_variables = {'format_instructions': parser.get_format_instructions()})

"""prompt = template.invoke({'topic':'blackholes'})



result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)"""

chain = template |model |parser
result = chain.invoke({'topic':'blackholes'})
print(result)