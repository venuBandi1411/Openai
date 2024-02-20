
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
import os
import streamlit as st


st.title("Langchain Demo")



# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'


llm = OpenAI(temperature=0.6)

#This code is With SerpAPIWrapper
search = SerpAPIWrapper()
input_text = st.text_input("Search topic u want....")

if input_text:
    st.write(search.run(input_text))


# This code without SerpAPIWrapper
# search = SerpAPIWrapper()
# print("Enter The Question : -")
# try:
#     query = input()
#     print("Question:", query)
#     response = search.run(query)
#     print("Response:", response)
# except Exception as e:
#     print("Error:", e)




   
