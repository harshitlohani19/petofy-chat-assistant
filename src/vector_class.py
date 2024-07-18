import chromadb
from loader import load_json
from src.embedder import Embedder

data = load_json()


class vector:
    def __init__(self, name=None, loc=None) -> None:
        self.name = name
        self.loc = loc

    def vector_name(self) -> str:
        if not self.name:
            self.name = input(str("Enter Collection name: "))
        return self.name

    def vector_loc(self) -> str:
        if not self.loc:
            self.loc = input(str("enter path: "))
        return self.loc

    def db_create(self):
        client = chromadb.PersistentClient(path=f"{self.vector_loc()}")
        emb_fun = Embedder.get_model(self)
        db_name = self.vector_name()
        chunks = self.splitter(data)

        # Generate unique IDs for each document
        ids = [f"doc{i+1}" for i in range(len(chunks))]

        try:
            collection = client.get_collection(name=db_name, embedding_function=emb_fun)
            s = input(str("Collection already Exists.Data Update required? (yes/no): "))
            if s.lower() == "yes":
                collection.upsert(documents=chunks, ids=ids)
            else:
                print("No update performed.")
        except ValueError:
            print("Collection does not exist, creating one and adding data to it: ")
            collection = client.create_collection(
                name=db_name, embedding_function=emb_fun
            )
            if chunks and ids:
                collection.add(documents=chunks, ids=ids)
            else:
                print("No data to add. Chunks or IDs list is empty.")
        # test = collection.peek()["embeddings"]
        # print(test)
        return collection


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
