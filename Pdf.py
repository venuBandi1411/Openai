from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
import os
os.environ["OPENAI_API_KEY"] = "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"


# provide the path of  pdf file/files.
pdfreader = PdfReader('budget_speech.pdf')

from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# print(raw_text)

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

len(texts)

embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "Vision for Amrit Kaal"
docs = document_search.similarity_search(query)
print(chain.run(input_documents=docs, question=query))