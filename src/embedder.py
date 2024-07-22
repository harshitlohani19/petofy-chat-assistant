from abc import ABC,abstractmethod

class Embedder(ABC):

    @abstractmethod
    def custom_embedder(self):
        pass
    
    @abstractmethod
    def azure_embeddings(self):
        pass

    @abstractmethod
    def sentence_transformers(self):
        pass

    @abstractmethod
    def hugging_face(self):
        pass
