import os
from openai import AzureOpenAI
from loader import load_json
from client import client_env

client = client_env()
combined_data = load_json()


def generate_embeddings(combined_data):
    for c in combined_data:
        abcd = client.embeddings.create(input=c, model="text-embedding")
        embeddings_data = abcd["data"][0]["embedding"]
        print(embeddings_data)
        return abcd


#     # Save embeddings to a JSON file
#     with open(output_file, "w") as file:
#         json.dump(embeddings, file, indent=4)


# generate_embeddings(combined_data)
