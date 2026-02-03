from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-ada-002", dimensions=32)

documents = [
    "delhi is the capital of india",
    "paris is the capital of france",
    "berlin is the capital of germany",
    "madrid is the capital of spain"
]
query = "capital of india?"

doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

index,score=sorted(list(enumerate(scores[0])), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score:", score)   