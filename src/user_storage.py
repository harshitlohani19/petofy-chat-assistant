import chromadb
from base_storage import Basestorage
from user_splitter import UserSplitAlgo
from loader import load_json

combined_data, data = load_json()

class VectorDB(Basestorage):
    
    def azure_index(self):
        pass

    def chromadb_creation(self, splitter, db_name, dbloc, emb_fun):
        client = chromadb.PersistentClient(path=f"{dbloc}")

        split_results = splitter.set_splitter(splitter.custom_splitter, data)

        collection = client.get_or_create_collection(
            name=db_name, embedding_function=emb_fun
        )

        for chunk, chunk_ids in split_results:
            # Ensure documents and ids have the same length
            if len(chunk) == len(chunk_ids):
                collection.add(documents=chunk, ids=chunk_ids)
            else:
                raise ValueError("Mismatch between number of documents and IDs")

        test = collection.peek()["embeddings"]
        print(test)
        return collection
    
    def set_database(self, splitter, db_name, dbloc, emb_fun, callback):
        result = callback(splitter, db_name, dbloc, emb_fun)
        return result
