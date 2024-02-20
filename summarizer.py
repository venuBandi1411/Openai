import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
import os
os.environ["OPENAI_API_KEY"] = "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"

# Initialize Ollama model
llm = OpenAI(temperature=0.6)

# Define PromptTemplate
template = '''Summarize this and make it concise and provide the bullet points and explain the each point for each subject for user interface:of the following speech:\n TEXT:'{speech}'''
summary_prompt = PromptTemplate(
    input_variables=["speech"],
    template=template,
)

# Initialize LLMChain
chain = LLMChain(llm=llm, prompt=summary_prompt, output_parser=StrOutputParser())

# Function to generate summary and bullet points
def generate_summary(speech):
    translation_result = chain({'speech': speech})
    summary = translation_result['text']
    bullet_points = translation_result['speech']
    return summary, bullet_points.replace('\n', '*')

# Streamlit app
def main():
    st.title("Text Summarizer")

    # Text input for speech
    speech_input = st.text_area("Enter the speech to summarize:", height=200)

    # Button to trigger summarization
    if st.button("Summarize") and speech_input:
        summary, bullet_points = generate_summary(speech_input)

        # Display summary and bullet points
        st.header("Summary:")
        st.write(summary)

        # st.header("Bullet Points:")
        # st.write(bullet_points)

if __name__ == "__main__":
    main()
