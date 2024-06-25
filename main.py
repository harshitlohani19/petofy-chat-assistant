import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
import json


client = AzureOpenAI(
    api_key="f398797cbb734cfdb1de68fdc68cae67",
    api_version="2024-02-01",
    azure_endpoint="https://petofy-test.openai.azure.com/",
)


temperature = 0
