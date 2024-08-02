from chromadb.utils import embedding_functions
from base_embedder import Embedder
from sentence_transformers import SentenceTransformer


class sen_transformer_embedder(Embedder):
    def embedder(self):
        # 1. Load a pretrained Sentence Transformer model
        model = SentenceTransformer("all-MiniLM-L12-v2")
        #embeddings=model.encode()
        return model
    
    def set_embedder(self, embedder_callback):
        return embedder_callback()
