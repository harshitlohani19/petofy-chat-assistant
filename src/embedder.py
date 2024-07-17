from chromadb.utils import embedding_functions


class Embedder:
    def __init__(self):
        self.model_name = "all-MiniLM-L6-v2"
        self.model = embedding_functions.SentenceTransformerEmbeddingFunction(
            self.model_name
        )
