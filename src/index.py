import json
import os
from pathmaker import env_path
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchFieldDataType,
)
from azure.search.documents import SearchClient
from vector import generate_embeddings
from client import client_env

client = client_env()
vectors = generate_embeddings()

# Load environment variables from the .env file
env_path = env_path()
load_dotenv(env_path)

endpoint = os.getenv("AZURE_ENDPOINT")
azure_search_key = os.getenv("AZURE_RESOURCE_KEY")


def create_index():
    # Define the index name
    index_name = "petofy_vector_data"

    client = SearchIndexClient(
        endpoint=endpoint, credential=AzureKeyCredential(azure_search_key)
    )

    try:
        # Check if the index already exists
        existing_index = client.get_index(index_name)
        if existing_index:
            print(f"Index '{index_name}' already exists. No action taken.")
            return
    except Exception as e:
        # If the index doesn't exist, an exception will be thrown, which we can ignore
        print(f"Index '{index_name}' does not exist. Creating a new one.")

    # Define the index schema
    fields = [
        SimpleField(name="index", type=SearchFieldDataType.String, key=True),
        SimpleField(name="object", type=SearchFieldDataType.String),
        SimpleField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Double),
        ),
    ]

    # Create the SearchIndex object
    index_schema = SearchIndex(
        name=index_name,
        fields=fields,
    )

    # Create the index in Azure Search
    try:
        result = client.create_index(index=index_schema)
        print(f"Index '{index_name}' created successfully!")
    except Exception as e:
        print(f"Failed to create index '{index_name}': {e}")

    client.close()


create_index()


def upload_to_index():
    # Reinitialize the client to interact with the newly created index
    search_client = SearchClient(
        endpoint=endpoint,
        index_name="petofy_vector_data",
        credential=AzureKeyCredential(azure_search_key),
    )
    # Load data from JSON file
    with open("vector_data.json", "r") as json_file:
        vectors = json.load(json_file)

    # Upload the batch to the Azure Search index
    result = search_client.upload_documents(documents=vectors)
    print("Documents uploaded")

    # Close the search client
    search_client.close()


upload_to_index()
