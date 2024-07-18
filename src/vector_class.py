import chromadb
from loader import load_json
from src.embedder import Embedder

data = load_json()


class vector_func:
    def __init__(self, name=None, loc=None) -> None:
        self.name = name
        self.loc = loc
        self.chunks = []
        self.combined_text = []

    def vector_name(self) -> str:
        if not self.name:
            self.name = input(str("Enter Collection name: "))
        return self.name

    def vector_loc(self) -> str:
        if not self.loc:
            self.loc = input(str("enter path: "))
        return self.loc

    def splitter(self, data) -> list:
        self.combined_text = []
        self.chunks = []
        # Combine Prompt and Response into a single document
        for item in data:
            for key, value in item.items():
                self.combined_text.append(str(value))  # Ensure all values are strings
        for i in range(0, len(self.combined_text), 100):
            chunk = " ".join(self.combined_text[i : i + 100])
            self.chunks.append(chunk)
        return self.chunks

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
