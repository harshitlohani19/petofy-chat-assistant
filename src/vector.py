from abc import ABC,abstractmethod
class BaseVector(ABC):

    @abstractmethod
    def vector_name(self,name):
        pass

    @abstractmethod
    def vector_loc(self,loc):
        pass



