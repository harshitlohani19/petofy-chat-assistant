from abc import ABC, abstractmethod

class Basesplitter(ABC):
    @abstractmethod    
    def chunk_size(self, chunks_size):
        pass

    @abstractmethod
    def custom_splitter(self,data,):
        pass
