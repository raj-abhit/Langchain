from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint



from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta", task="text-generation")

model = ChatHuggingFace(llm=llm,temperature=0.3, max_output_tokens=100)

result = model.invoke("capital of india?")

print(result.content)