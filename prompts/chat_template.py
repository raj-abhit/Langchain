from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate.from_messages([
    
    ('system', 'you are a helpful {domain} expert.'),
    ('human','explain in simple terms what is {topic}')
])

"""SystemMessage(content="You are a helpful {domain} expert."), HumanMessage(content="explain in symple terms what is{topic}")"""

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)