import json
from loader import load_json
from client import client_env

client = client_env()
combined_data = load_json()

vectors = []


def generate_embeddings():

    index = 0
    for c in combined_data:
        vector_data = client.embeddings.create(input=c, model="text-embedding")
        vectors.append(
            {
                "id": str(index),
                "text_chunk": str(c),
                "embedding": vector_data.data[0].embedding,
            }
        )
        index += 1
    # Write vectors to a JSON file
    with open("vector_data.json", "w") as json_file:
        json.dump(vectors, json_file)


generate_embeddings()
