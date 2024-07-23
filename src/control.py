from user_vector_config import VectorConfig
from user_splitter import UserSplitAlgo
from user_embedder import UserEmbedding
from user_storage import VectorDB
from loader import load_json

combined_data,data = load_json()
# config = VectorConfig.set_vector()

class FlowControl(VectorConfig):

    def __init__(self):
        self.name = None
        self.loc = None
        self.chunks = None
        self.emb_fun = None

    def vector_name(self, name):
        self.name = name
        return self.name

    def vector_loc(self, loc):
        self.loc = loc
        return self.loc
  

    def splitting_algo(self, chunks_size):

        splitter = UserSplitAlgo()
        self.chunks_size = chunks_size

        # set chunks size
        splitter.chunk_size(chunks_size)

        self.chunks= splitter.set_splitter(splitter.custom_splitter,data)
        return self.chunks
    
    def gen_embeddings(self):

        embedder=UserEmbedding()

        emb_fun = embedder.set_embedder(embedder.custom_embedder)
        #emb_data=emb_fun(self.chunks)
        self.emb_fun = emb_fun
        return self.emb_fun
    
    def storage_creation(self):
        vec_db=VectorDB
        db = vec_db.set_database(self,self.chunks, self.name, self.loc, self.emb_fun, vec_db.chromadb_creation)
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

        

