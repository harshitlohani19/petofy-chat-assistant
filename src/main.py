from base_vector import BaseVector
from user_splitter import ChunkSplitter
from user_embedder import sen_transformer_embedder
from user_storage import VectorDB
from loader import load_json

combined_data, data = load_json()


class FlowControl(BaseVector):
    def __init__(self) -> None:
        super().__init__()
        self.chunks_size = None
        self.emb_fun = None
        self.splitter = None
        self.embeddings=None

    def splitting_algo(self, chunks_size) -> None:
        self.chunks_size = chunks_size
        self.splitter = ChunkSplitter()
        self.splitter.chunk_size(chunks_size)

    def gen_embeddings(self):
        embedder_inst = sen_transformer_embedder()
        
        self.emb_fun = embedder_inst.set_embedder(embedder_inst.embedder)
        return self.emb_fun

    def storage_creation(self) -> None:
        vec_db = VectorDB()
        db=vec_db.set_database(self.splitter, self.vector_name, self.vector_loc, self.emb_fun,vec_db.chroma_db_creation)
        # test = db.peek()["embeddings"]
        # print(test)

def main():
    flow = FlowControl()

    flow.vector_name = input("Enter DB name: ")

    flow.vector_loc = input("Enter location: ")

    chunks_size = int(input("enter chunk size: "))
    flow.splitting_algo(chunks_size)

    flow.gen_embeddings()

    flow.storage_creation()

if __name__ == "__main__":
    main()
