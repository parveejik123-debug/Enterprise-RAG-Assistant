import os
import glob

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


folders = glob.glob("../../cognizant/data/*.md")

documents = []

for folder in folders:
    doc_type = os.path.basename(folder)
    loader = TextLoader(folder, encoding="utf-8")
    folder_docs = loader.load()

    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        documents.append(doc)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)