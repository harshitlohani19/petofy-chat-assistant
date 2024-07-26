from user_vector_config import VectorConfig
from user_splitter import ChunkSplitter
from user_embedder import ChromaEmbedder
from user_storage import VectorDB

class FlowControl:
    
    def __init__(self, vector_config, splitter, embedder, storage):
        self.vector_config = vector_config
        self.splitter = splitter
        self.embedder = embedder
        self.storage = storage

    def vector_name(self, name):
        return self.vector_config.vector_name(name)

    def vector_loc(self, loc):
        return self.vector_config.vector_loc(loc)

    def splitting_algo(self, chunk_size):
        self.splitter.chunk_size(chunk_size)

    def gen_embeddings(self):
        return self.embedder.set_embedder(self.embedder.embedder)

    def storage_creation(self):
        return self.storage.set_database(
            self.splitter, self.vector_config.name, self.vector_config.loc, self.gen_embeddings(), self.storage.db_creation
        )
