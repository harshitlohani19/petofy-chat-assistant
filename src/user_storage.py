import chromadb
from base_storage import Basestorage
from user_splitter import UserSplitAlgo
from loader import load_json

combined_data, data = load_json()



class VectorDB(Basestorage):
    
    splitter = UserSplitAlgo()

    def db_creation(self, splitter,db_name, dbloc, emb_fun):

        client = chromadb.PersistentClient(path=f"{dbloc}")

        split_results=splitter.set_splitter(splitter.custom_splitter, data)

        collection = client.get_or_create_collection(
            name=db_name, embedding_function=emb_fun
        )
        for chunk, chunk_id in split_results:
            collection.add(documents=chunk, ids=chunk_id)

        return collection
    
    def set_database(self, splitter, db_name, dbloc, emb_fun, callback):
        result = callback(splitter, db_name, dbloc, emb_fun)
        return result
