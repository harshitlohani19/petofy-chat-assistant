from user_vector_config import VectorConfig
from user_splitter import UserSplitAlgo
from user_embedder import UserEmbedding
from user_storage import VectorDB
from loader import load_json

combined_data,data = load_json()

class FlowControl(VectorConfig):

    def __init__(self) -> None:
        self.name = None
        self.loc = None
        self.chunks = None
        self.emb_fun = None
        self.chunk = None
        self.ids=None
        self.splitter=None

    def vector_name(self, name) -> str:
        self.name = name
        return self.name

    def vector_loc(self, loc) -> str:
        self.loc = loc
        return self.loc
  

    def splitting_algo(self, chunks_size):
        """
        returns data in chunks
        """
        
        self.chunks_size = chunks_size
        self.splitter = UserSplitAlgo()

        # set chunks size
        self.splitter.chunk_size(chunks_size)

        # self.chunks = splitter.set_splitter(splitter.custom_splitter, data)
        # for self.chunk in self.chunks:
        #      yield self.chunk, self.ids
    def gen_embeddings(self):
        """
        returns embedding function
        """
        embedder=UserEmbedding()
        emb_fun = embedder.set_embedder(embedder.custom_embedder)
        #emb_data=emb_fun(self.chunks)
        self.emb_fun = emb_fun
        return self.emb_fun
    
    def storage_creation(self) -> None:
        vec_db=VectorDB()
        db = vec_db.set_database(self.splitter,self.name, self.loc, self.emb_fun, vec_db.chromadb_creation)
        #print(self.chunk)
        #print(self.ids)
        print("Db created successfully")


def main():
    flow = FlowControl()

    name = input(str("enter db name: "))
    flow.vector_name(name)

    loc = input(str("enter location: "))
    flow.vector_loc(loc)

    chunks_size = int(input("enter chunk size: "))
    flow.splitting_algo(chunks_size)

    flow.gen_embeddings()
    
    flow.storage_creation()

if __name__== "__main__":
    main()

        

