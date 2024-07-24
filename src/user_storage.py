import chromadb
from base_storage import Basestorage
from user_splitter import UserSplitAlgo
from loader import load_json

splitter =UserSplitAlgo()
combined_data, data = load_json()


class VectorDB(Basestorage):
    
    def azure_index():
        pass

    def chromadb_creation(self, splitter,db_name, dbloc, emb_fun):

        client = chromadb.PersistentClient(path=f"{dbloc}")

        split_results=splitter.set_splitter(splitter.custom_splitter, data)


        collection = client.get_or_create_collection(
            name=db_name, embedding_function=emb_fun
        )
        for chunk, id in split_results:
            collection.add(documents=chunk, ids=[str(id)])
        test = collection.peek()["embeddings"]
        # print(self.chunks)
        # print(self.ids)
        print(test)
        return collection
    

    def set_database(self, splitter,db_name, dbloc, emb_fun, callback):
        result = callback(splitter,db_name, dbloc, emb_fun)
        return result
