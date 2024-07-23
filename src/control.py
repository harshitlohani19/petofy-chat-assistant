from user_vector_config import VectorConfig
from user_splitter import UserSplitAlgo
from user_embedder import UserEmbedding
from user_storage import VectorDB
from loader import load_json

combined_data,data = load_json()
# config = VectorConfig.set_vector()

class FlowControl(VectorConfig):

    def __init__():
        pass

    def vector_name(self, name):
        name = input(str("enter db name"))
        self.name = name
        return self.name

    def vector_loc(self, loc):
        loc = input(str("Enter location"))
        self.loc = loc
        return self.loc
  

    def splitting_algo(self):
        chunks_size=input(str("Enter chunk size"))
        chunk_size=UserSplitAlgo.chunk_size(chunks_size)
        self.chunks = UserSplitAlgo.set_splitter(self,UserSplitAlgo.custom_splitter,data)
        return self.chunks
    
    def gen_embeddings(self):
        emb_fun = UserEmbedding.set_embedder(self,UserEmbedding.custom_embedder)
        #emb_data=emb_fun(self.chunks)
        self.emb_fun=emb_fun
        return self.emb_fun
    
    def storage_creation(self):
        db = VectorDB.set_database(self, self.chunks, self.name, self.loc,self.emb_fun)


    vector_name()
    vector_loc()
    splitting_algo()
    gen_embeddings()
    storage_creation()

    

