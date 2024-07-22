#import chromadb
from splitting import Textsplitter
from loader import load_json
#from src.embedder import Embedder

splitter=Textsplitter()
class Vector:

    def vector_name(self,name):
        self.name=name
        return name

    def vector_loc(self,loc):
        self.loc=loc
        return loc

    def set_vector(self,callback,*args,**kwargs):
        result=callback(*args,**kwargs)
        print(result)



    def db_create(self):
        client = chromadb.PersistentClient(path=f"{self.loc}")
        emb_fun = Embedder.get_model(self)
        db_name = self.name
        chunks = splitter.

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

