import chromadb
from chromadb.utils import embedding_functions


class Embedder:
    def __init__(self, model):
        self.model = model

    def get_model(self):
        self.model = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        return self.model
