from langchain_groq import ChatGroq
#from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

chat_history = []

"""
chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]
"""
while True:
    user_input = input('you:')
    chat_history.append({user_input})
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append({result.content})
    print("AI: ",result.content)#current respose
    
print(chat_history)#prints when exited

"""
while True:
    user_input = input('you:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)#current respose
    
print(chat_history)#prints when exited"""