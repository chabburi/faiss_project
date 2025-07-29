import json
import os
import boto3
import pypdf
from pypdf import PdfReader
from langchain.llms.bedrock import Bedrock
from langchain_aws import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

# Defining bedrock client
bedrock_client = boto3.client("bedrock-runtime")


# Initialize embeddings model
bedrock_embeddings= BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0",
    client=bedrock_client
)


#Splitting the ..
def document_text_splitter(text):
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs= text_splitter.split_text(text)
    docs=text_splitter.create_documents(docs)
    return docs

#Creating embeddings and storing them in local
def storing_embeddings(docs):
    if os.path.exists("faiss_index") and os.path.isdir("faiss_index"):
        existing_index=FAISS.load_local("faiss_index",bedrock_embeddings,allow_dangerous_deserialization=True)
        existing_index.add_documents(docs)
        existing_index.save_local("faiss_index")
    else:
        vectorstore_faiss=FAISS.from_documents(
            docs,
            bedrock_embeddings
        )
        vectorstore_faiss.save_local("faiss_index")
    return "Embeddings created and Stored successfully!"

#Main function process end to end flow for creating embeddings
def create_embeddings(content):
    chunks = document_text_splitter(content)
    return storing_embeddings(chunks)


