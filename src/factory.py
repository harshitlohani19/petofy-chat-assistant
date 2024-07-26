from user_vector_config import VectorConfig
from user_splitter import ChunkSplitter
from user_embedder import ChromaEmbedder
from user_storage import VectorDB

class Factory:
    @staticmethod
    def create_vector_config():
        return VectorConfig()

    @staticmethod
    def create_splitter():
        return ChunkSplitter()

    @staticmethod
    def create_embedder():
        return ChromaEmbedder()

    @staticmethod
    def create_storage():
        return VectorDB()
