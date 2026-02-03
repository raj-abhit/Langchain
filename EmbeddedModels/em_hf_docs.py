from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")



docs=[
    "delhi is the capital of india",
    "paris is the capital of france",
    "berlin is the capital of germany"
]

vector = embeddings.embed_documents(docs)

print(str(vector))