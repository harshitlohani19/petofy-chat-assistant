from abc import ABC, abstractmethod

class BaseStorage(ABC):
    @abstractmethod
    def db_creation(self, splitter_instance, db_name dbloc emb_fun) -> None:
        pass
