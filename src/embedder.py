import os
import chromadb
from chromadb.utils import embedding_functions
import json
from dotenv import load_dotenv
from pathmaker import env_path
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ExhaustiveKnnAlgorithmConfiguration,
    ExhaustiveKnnParameters,
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    HnswParameters,
    VectorSearchAlgorithmKind,
    VectorSearchAlgorithmMetric,
    VectorSearchProfile,
)
from azure.search.documents import SearchClient

# from vector import generate_embeddings
from client import client_env

client = client_env()

# Load environment variables from the .env file
env_path = env_path()
load_dotenv(env_path)

service_endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_RESOURCE_KEY")

class Embedder:
    def __init__(self, model):
        self.model = model

    def get_model():
        print("Choose type of Embedding:")
        print("1: Azure Embedding, 2:Sentance Transformer,3: ")
    def azure_embeddings():


    def sentance_transformers():

    def hugging_face():
