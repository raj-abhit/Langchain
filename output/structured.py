from langchain_groq import ChatGroq

from dotenv import load_dotenv
from typing import Optional, TypedDict,Annotated

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

#schema
class Review(TypedDict):
    #rating: int
    #key: Annotated[str, "A unique identifier for the review"]
    summary: Annotated[str, "give me A brief summary of the review"]
    sentiment: Annotated[str,"return sentiment of review either negative ,positive or neutral"]
    pros: Annotated[Optional[str],"list of pros in the review"]
    
    
structured_model = model.with_structured_output(Review)



result = structured_model.invoke("""The movie was fantastic! I really enjoyed the plot and the characters were well developed. The cinematography was stunning and the soundtrack perfectly complemented the scenes. Overall, it was a great experience and I would highly recommend it to others.""")

print(result)
#print(result['summary'])
#print(result['sentiment'])
#print(result['rating'])