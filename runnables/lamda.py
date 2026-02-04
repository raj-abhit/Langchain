from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

"""def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke("This is a sample sentence to count words."))  # Output: 8"""

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)


joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({'joke':RunnablePassthrough(),'word_count':RunnableLambda(lambda x: len(x.split()))})
final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'ai'})

final_result = """{}\n word count: {}""".format(result['joke'], result['word_count'])
print(final_result) 