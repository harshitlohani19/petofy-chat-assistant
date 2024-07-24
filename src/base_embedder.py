from abc import ABC,abstractmethod

class Embedder(ABC):

    @abstractmethod
    def custom_embedder(self):
        pass
    