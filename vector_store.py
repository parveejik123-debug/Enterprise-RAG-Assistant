import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import db_name
from data_loader import chunks


embaddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-V2"
)

if os.path.exists(db_name):
    Chroma(
        persist_directory=db_name,
        embedding_function=embaddings
    ).delete_collection()

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embaddings,
    persist_directory=db_name
)

vectorstore = Chroma(
    persist_directory=db_name,
    embedding_function=embaddings
)

retriever = vectorstore.as_retriever()