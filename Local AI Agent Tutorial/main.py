from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")
template = """
You are an expert in answering questions about pizza restaurent

Here are some relevant reviews: {reviews}
e
Here is the question to answer: {question}
""" 
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True: 
    print("\n\n----------------------------------------")
    question = input("Ask your question (q to exit) : ")
    print("\n\n----------------------------------------")

    if question == "q": 
       break 

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)

