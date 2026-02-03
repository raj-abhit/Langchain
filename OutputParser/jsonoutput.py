from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

"""llm  =HuggingFaceEndpoint(repo_id = "google/gemma-2b-it",
                          task ="text-generation"
)

model = ChatHuggingFace(llm = llm)
"""

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

"""
parser = JsonOutputParser()
template = PromptTemplate(
    template = 'Give me the name ,age and city of a fictional person\n {format_instructions}',
    input_variables = [],
    partial_variables = {'format_instructions':parser.get_format_instructions()}
)

"""prompt = template.format()

#print(prompt)
result = model.invoke(prompt)
#print(result)

final_result = parser.parse(result.content)

print(final_result)
print(type(final_result))
"""

chain = template | model | parser
result = chain.invoke({})
print(result)
print(type(result))