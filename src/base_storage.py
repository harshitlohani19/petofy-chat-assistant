from abc import ABC, abstractmethod

class BaseStorage(ABC):
    @abstractmethod
    def db_creation(self, splitter_instance, db_name: str, dbloc: str, emb_fun) -> None:
        pass
