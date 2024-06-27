import os
from openai import AzureOpenAI
from loader import load_json
from client import client_env

client = client_env()
combined_data = load_json()


def generate_embeddings(combined_data):
    for c in combined_data:
        abcd = client.embeddings.create(input=c, model="text-embedding")

    return abcd


generate_embeddings(combined_data)
