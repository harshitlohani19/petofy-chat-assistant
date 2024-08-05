from chromadb.utils import embedding_functions
from base_embedder import Embedder

class ChromaEmbedder(Embedder):
    def embedder(self):
        emb = embedding_functions.DefaultEmbeddingFunction()
        return emb

    def set_embedder(self, embedder_callback):
        return embedder_callback()
