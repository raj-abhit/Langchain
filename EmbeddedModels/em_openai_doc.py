from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

emmbedings=OpenAIEmbeddings(model = "text-embedding-ada-002",dimensions=32)

docs=[
    "delhi is the capital of india",
    "paris is the capital of france",
    "berlin is the capital of germany"
]

result = emmbedings.embed_documents(docs)

print(str(result))