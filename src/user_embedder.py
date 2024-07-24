from chromadb.utils import embedding_functions
from base_embedder import Embedder

class UserEmbedding(Embedder):

    def azure_embeddings(self):
        pass
    def sentence_transformers(self):
        pass

    def custom_embedder(self):
        emb = embedding_functions.DefaultEmbeddingFunction()
        # emb_data=emb(chunks)
        return emb
    

    def set_embedder(self, embedder_callback):
        result = embedder_callback()
        return result
