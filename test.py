import os
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchFieldDataType,
)
from azure.search.documents.models import IndexDocumentsBatch, IndexingResult
from azure.openai import OpenAIClient
from azure.identity import DefaultAzureCredential
import numpy as np


endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ["CHAT_COMPLETIONS_DEPLOYMENT_NAME"]


# Load environment variables from the .env file
env_path = find_dotenv("config/.env")
load_dotenv(env_path)

# Environment variables
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Configure OpenAI API for Azure
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2024-02-01"
openai.api_key = AZURE_OPENAI_API_KEY


# Function to generate embeddings using OpenAI
def generate_embeddings(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002",  # Adjust this if your deployment name differs
    )
    return response["data"][0]["embedding"]


# Create an Azure Search Index with the necessary fields
def create_search_index(index_name, client):
    fields = [
        SimpleField(
            name="documentId",
            type=SearchFieldDataType.String,
            filterable=True,
            sortable=True,
            key=True,
        ),
        SearchableField(name="content", type=SearchFieldDataType.String),
        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_configuration="my-vector-config",
        ),
    ]
    vector_search = VectorSearch(
        algorithm_configurations=[
            {"name": "my-vector-config", "algorithm": "vector-dot-product"}
        ]
    )
    index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
    result = client.create_index(index)
    print(f"Index created: {result}")


# Load all JSON files from a specified directory
def load_json_files(directory_path):
    all_files = glob.glob(os.path.join(directory_path, "*.json"))
    documents = []
    for file in all_files:
        with open(file, "r") as f:
            data = json.load(f)
            documents.append(data)
    return documents


# Embed the documents and prepare for upload
def embed_documents(documents):
    for doc in documents:
        if "content" in doc:
            doc["embedding"] = generate_embeddings(doc["content"])
    return documents


# Upload documents to the Azure Search Index
def upload_documents_to_index(documents, index_name, search_endpoint, search_api_key):
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=index_name,
        credential=AzureKeyCredential(search_api_key),
    )
    result = search_client.upload_documents(documents)
    print(f"Upload result: {result}")


# Query the Azure Search Index using a vector
def query_search_index(query, index_name, search_endpoint, search_api_key):
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=index_name,
        credential=AzureKeyCredential(search_api_key),
    )
    vector = Vector(value=generate_embeddings(query), k=2, fields="embedding")
    results = search_client.search(
        search_text=None,
        vectors=[vector],
        select=["content"],
    )
    return results


# Main script to run the whole process
if __name__ == "__main__":
    # Step 1: Create the search index
    search_index_client = SearchIndexClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        credential=AzureKeyCredential(AZURE_SEARCH_API_KEY),
    )
    create_search_index(INDEX_NAME, search_index_client)

    # Step 2: Load JSON files from the directory
    documents = load_json_files("dataset/data")

    # Step 3: Embed the documents
    embedded_documents = embed_documents(documents)

    # Step 4: Upload embedded documents to Azure Search Index
    upload_documents_to_index(
        embedded_documents, INDEX_NAME, AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_API_KEY
    )

    # Step 5: Query the search index
    query_text = "What information does this handbook have?"
    results = query_search_index(
        query_text, INDEX_NAME, AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_API_KEY
    )

    # Collecting results
    input_text = " "
    for result in results:
        input_text += result["content"] + " "

    print(f"Aggregated search results: {input_text}")
