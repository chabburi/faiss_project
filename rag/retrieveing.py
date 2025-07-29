#Import the requiews packages
import json
import os
import boto3
from langchain_aws import BedrockEmbeddings
from langchain.vectorstores import FAISS


#User Prompt to return the answer as per input from the retrieved chunks
Prompt="""
You are a job search assistant, your task is to help the user in answering the questions from the provided chunks. Based on the
user query and chunks provided try to answer the user question. Do not try to add any extra information or provide false 
information on your own. Make sure your tone is polite while answering the user query.
Input query: {},
Document Chunks: {}
"""

# Initialize AWS Bedrock client
bedrock_client = boto3.client("bedrock-runtime")
bedrock = boto3.client("bedrock-runtime")

# Initialize embeddings model
bedrock_embeddings = BedrockEmbeddings(
    model_id = "amazon.titan-embed-text-v2:0",
    client = bedrock_client
)

#Function for converting the user query into embeddings
def create_embeddings(question):
    q_embedding = bedrock_embeddings.embed_query(question)
    return q_embedding
    
#Function to fetch the relevant chunks from Faiss-Embeddings
def fetch_relevant_chunks(q_embeddings):
    vector_store=FAISS.load_local("faiss_index",bedrock_embeddings,allow_dangerous_deserialization=True)
    docs=vector_store.similarity_search_by_vector(q_embeddings,k=3)
    return docs

#Invoking model with prompt to get response
def invoke_model_response(prompt):
    body = json.dumps({
    "messages":[
        {
        "role":"user",
        "content":[
            {
            "text":prompt
            }
        ]
    }        
    ]
    })
    model_id="us.amazon.nova-premier-v1:0"
    accept = "application/json"
    content_type = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=model_id, accept=accept, contentType=content_type
    )
    response_body = json.loads(response.get("body").read())
    return response_body['output']['message']['content'][0]['text']

#Main function to read user input and return the result.
def answering_user_question(question):
    question_embedding = create_embeddings(question)
    documents = fetch_relevant_chunks(question_embedding)
    prompt=Prompt.format(question , documents)
    answer = invoke_model_response(prompt)
    return answer
    
    
    
