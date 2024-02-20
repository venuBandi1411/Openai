from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain import OpenAI, VectorDBQA

import os
import openai



loader = UnstructuredFileLoader('budget_speech.pdf')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(api_key=os.environ['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'])
doc_search = Chroma.from_documents(texts, embeddings)
chain = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=doc_search)
query="How many years they have targeted each and every household?"
chain.run(query)
