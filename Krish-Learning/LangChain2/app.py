# Simple GenAI App using LangChain
import os
from dotenv import load_dotenv 

from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith tracking. 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template - 

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, please respond to questions asked."),
    ("user", "Question: {question}"),
])

st.title("Langchain demo with Gemma Model")
input_text = st.text_input("What question do you have?") 

if input_text:
    llm=Ollama(model="gemma:2b")
    output_parser = StrOutputParser() 
    chain = prompt | llm | output_parser
    type(chain)
    response = chain.invoke({"question": input_text})
    st.write(response)




