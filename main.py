import os
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient


# Load environment variables from the .env file
env_path = find_dotenv("config/.env")
load_dotenv(env_path)


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)
