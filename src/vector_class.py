import chromadb
from loader import load_json
from src.embedder import Embedder

data = load_json()


class vector_func:
    def __init__(self, name, loc, chunks, combined_text) -> None:
        self.name = name
        self.loc = loc
        self.chunks = chunks
        self.combined_text = combined_text

    def vector_name(self) -> str:
        self.name = input(str("Enter Collection name: "))
        return self.name

    def vector_loc(self) -> str:
        self.loc = input(str("enter path: "))
        return self.loc

    def splitter(self, data) -> list:
        # Combine Prompt and Response into a single document
        for item in data:
            for key, value in item.items():
                self.combined_text.append(value)

        for i in range(0, len(self.combined_text), 100):
            chunk = self.combined_text[i : i + 100]
            self.chunks.append(chunk)
        return self.chunks

    def db_create(self):
        client = chromadb.PersistentClient(path=f"{self.vector_loc()}")
        emb_fun = Embedder().model_name
        db_name = self.vector_name()
        # Generate unique IDs for each document
        ids = [f"doc{i+1}" for i in range(len(self.combined_text))]
        try:
            collection = client.get_collection(name=db_name, embedding_function=emb_fun)
            s = input(str("Data Update required?"))
            if s == "yes":
                collection.upsert(documents=self.splitter(data), ids=ids)
            else:
                pass
        except:
            print("Collection Does not exist, creating one and adding data to it: ")
            collection = client.create_collection(
                name=db_name, embedding_function=emb_fun
            )
            collection.add(documents=self.splitter(data), ids=ids)

        collection = client.get_collection(name=db_name, embedding_function=emb_fun)

        return collection
