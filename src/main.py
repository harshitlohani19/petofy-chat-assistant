from user_vector_config import VectorConfig
from user_splitter import ChunkSplitter
from user_embedder import ChromaEmbedder
from user_storage import VectorDB
from loader import load_json

combined_data, data = load_json()

class FlowControl(VectorConfig):
    def __init__(self) -> None:
        super().__init__()
        self.chunks_size = None
        self.emb_fun = None
        self.splitter = None

    def splitting_algo(self, chunks_size: int) -> None:
        self.chunks_size = chunks_size
        self.splitter = ChunkSplitter()
        self.splitter.chunk_size(chunks_size)

    def gen_embeddings(self):
        embedder = ChromaEmbedder()
        emb_fun = embedder.set_embedder(embedder.embedder)
        self.emb_fun = emb_fun
        return self.emb_fun

    def storage_creation(self) -> None:
        vec_db = VectorDB()
        db = vec_db.set_database(self.splitter, self.vector_name, self.vector_loc, self.emb_fun, vec_db.db_creation)
        # test = db.peek()["embeddings"]
        # print(test)


def main():
    flow = FlowControl()

    name = input(str("Enter DB name: "))
    flow.vector_name = name

    loc = input(str("Enter location: "))
    flow.vector_loc = loc

    chunks_size = int(input("Enter chunk size: "))
    flow.splitting_algo(chunks_size)

    flow.gen_embeddings()
    flow.storage_creation()


if __name__ == "__main__":

    main()
