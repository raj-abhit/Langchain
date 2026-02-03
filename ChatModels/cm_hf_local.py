from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(model_id="HuggingFaceH4/zephyr-7b-beta", task="text-generation",model_kwargs=dict(max_new_tokens=100, temperature=0.3))

model = ChatHuggingFace(llm=llm)

result = model.invoke("capital of india?")

print(result.content)