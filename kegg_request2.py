import os
import getpass
import requests
from langchain.openai import ChatOpenAI

# Set environment variables for API keys
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter OpenAI API Key: ")

# Function to query the KEGG database
def query_kegg(pathway_id):
    """Query the KEGG database for information on a specific pathway."""
    base_url = "http://rest.kegg.jp/get/"
    response = requests.get(f"{base_url}{pathway_id}")
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data: {response.text}")
        return None

# Function to perform RAG with the queried KEGG data
def perform_rag_with_kegg(question):
    """Perform Retrieval-Augmented Generation using KEGG data as context."""
    # Query the KEGG database for glycolysis pathway information as an example
    pathway_info = query_kegg("path:map00010")  # Glycolysis / Gluconeogenesis
    if not pathway_info:
        return "Could not retrieve pathway information from KEGG."
    
    # Directly use the KEGG pathway information as context for the LLM query
    formatted_input = f"Context: {pathway_info}\nQuestion: {question}"
    llm_response = llm(formatted_input)
    return llm_response

# Initialize the LLM (ChatGPT) with OpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Example usage: Asking about glycolysis based on KEGG pathway info
question = "What is the role of ATP in glycolysis?"
response = perform_rag_with_kegg(question)
print(response)