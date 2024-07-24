from abc import ABC,abstractmethod

class Embedder(ABC):

    @abstractmethod
    def embedder(self):
        pass
    