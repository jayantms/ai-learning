from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from dotenv import load_dotenv 

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY") 

llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)
response = llm.invoke("What is LangChain?")

## Create a prompt template
system_template = "Translate the following into {language} :"

prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "Question: {question}"),
])

parser = StrOutputParser() 

## Create a chain. 
chain = prompt | llm | parser 
response = chain.invoke({"language":"French", "question":"What is LangChain?"})

## App definition
app = FastAPI(title="Lanchain server", 
              version="1.0",
              description="A simple API server using Langchain runnable interface") 

## Addin chain routes 
add_routes(app, chain, path="/chain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    

