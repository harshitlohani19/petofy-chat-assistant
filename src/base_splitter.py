from abc import ABC, abstractmethod

class BaseSplitter(ABC):
    @abstractmethod
    def chunk_size(self, chunks_size) -> int:
        pass

    @abstractmethod
    def splitter(self, data) -> None:
        pass
