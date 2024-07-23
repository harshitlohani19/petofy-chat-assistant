import chromadb
from base_storage import Basestorage

class VectorDB(Basestorage):
    
    def azure_index():
        pass 

    def chromadb_creation(self, chunks, db_name, dbloc, emb_fun):
        client = chromadb.PersistentClient(path=f"{dbloc}")
        # Generate unique IDs for each document
        ids = [f"doc{i+1}" for i in range(len(chunks))]

        collection = client.get_or_create_collection(
            name=db_name, embedding_function=emb_fun
        )
        if chunks and ids:
            for s in chunks:
                # Generate unique IDs for each document
                ids = [f"doc{i+1}" for i in range(len(s))]
                collection.add(documents=s, ids=ids)
        else:
            print("No data to add. Chunks or IDs list is empty.")
        test = collection.peek()["embeddings"]
        #print(test)
        return collection

    def set_database(self, chunks, db_name, dbloc, emb_fun, callback):
        result = callback(self, chunks, db_name, dbloc, emb_fun)
        return result
