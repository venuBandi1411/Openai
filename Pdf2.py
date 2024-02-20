import os
import openai
from PyPDF2 import PdfReader

# Load PDF file and extract text
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Specify your OpenAI API key here
openai.api_key = "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"

pdf_file_path = 'RohitSharma.pdf'
text_from_pdf = extract_text_from_pdf(pdf_file_path)

# Example question (modify as needed)
question = "What is Rohit Sharma birthdate?"

# Use OpenAI API to get answers
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # changed engine to 'davinci'
    prompt=text_from_pdf,
    max_tokens=100,
    temperature=0.5,
    stop=["\n"]
)

# Extract the answer from the response
answer = response.choices[0].text.strip()  # Extracting the text from the response

print(f"Answer to '{question}': {answer}")
