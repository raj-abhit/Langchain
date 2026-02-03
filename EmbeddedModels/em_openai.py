from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

emmbedings=OpenAIEmbeddings(model = "text-embedding-ada-002",dimensions=32)

result = emmbedings.embed_query("capital of india?")

print(str(result))