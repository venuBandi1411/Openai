import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

st.title("Langchain Demo")

# Set OpenAI and SerpAPI API keys
os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = 'b5324d97a4c820c624c6eaa740bc94a5d059412eb4bf8d58ab416875f03fbc53'

llm = OpenAI(temperature=0.6)

search = SerpAPIWrapper()

input_text = st.text_input("Search topic you want....")
submit_button = st.button("Submit")

prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a relevant image for: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)

if input_text and submit_button:
    try:
        result = search.run(input_text)
        st.write("Generated text:", result)
        generated_text =DallEAPIWrapper().run(chain.run(image_desc=input_text))
        print("Image : -"+generated_text)
        st.image(generated_text)
        
        
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
