from chromadb.utils import embedding_functions
from base_embedder import Embedder

class UserEmbedding(Embedder):

    def custom_embedder(self):
        emb = embedding_functions.DefaultEmbeddingFunction()
        #emb_data=emb(chunks)
        return emb

    def set_embedder(self, embedder_callback, chunks):
        result = embedder_callback(chunks)
        return result
