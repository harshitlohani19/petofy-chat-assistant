from abc import ABC,abstractmethod

class Embedder(ABC):

    def custom_embedder(self):
        pass

    def azure_embeddings(self):
        pass

    def sentance_transformers(self):
        pass

    def hugging_face(self):
        pass
