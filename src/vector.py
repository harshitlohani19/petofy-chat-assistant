from abc import ABC,abstractmethod
class Vector(ABC):

    @abstractmethod
    def vector_name(self,name):
        pass

    @abstractmethod
    def vector_loc(self,loc):
        pass



