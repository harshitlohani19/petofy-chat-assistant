# env_setup.py
import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.openai import OpenAIClient
from azure.identity import DefaultAzureCredential

# Load environment variables from the .env file
load_dotenv()

# Retrieve values from environment variables
SEARCH_SERVICE_NAME = os.getenv("SEARCH_SERVICE_NAME")
INDEX_NAME = "petofy-test-h1"
SEARCH_API_KEY = os.getenv("AZURE_RESOURCE_KEY")
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DOCUMENTS_PATH = (
    "/home/harshitlohani/Desktop/Projects/petofy-chat-assistant/dataset/data"
)

# Set up Azure Cognitive Search client
search_client = SearchClient(
    endpoint=f"https://{SEARCH_SERVICE_NAME}.search.windows.net",
    index_name=INDEX__NAME,
    credential=DefaultAzureCredential(),
)

# Set up Azure Cognitive Search index client
search_index_client = SearchIndexClient(
    endpoint=f"https://{SEARCH_SERVICE_NAME}.search.windows.net",
    credential=DefaultAzureCredential(),
)

# Set up Azure OpenAI client
openai_client = OpenAIClient(
    endpoint=OPENAI_ENDPOINT, credential=DefaultAzureCredential()
)
