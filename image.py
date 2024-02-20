from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = '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'
llm = OpenAI(temperature=0.9)

# Shortened the prompt further
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Pic of {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)

image_url = DallEAPIWrapper().run(chain.run("Mahesh Babu"))
print(image_url)
