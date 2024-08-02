from abc import ABC, abstractmethod

class Embedder(ABC):
    @abstractmethod
    def embedder(self):
        pass

    def set_embedder(self, embedder_callback):
        return embedder_callback()