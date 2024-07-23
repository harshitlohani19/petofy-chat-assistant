from abc import ABC,abstractmethod

class Basestorage(ABC):

    @abstractmethod
    def chromadb_creation():
        pass
    @abstractmethod
    def azure_index():
        pass