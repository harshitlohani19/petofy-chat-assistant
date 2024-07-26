from abc import ABC, abstractmethod

class BaseVector(ABC):
    def __init__(self) -> None:
        self.name = None
        self.loc = None

    @property
    def vector_name(self) -> str:
        """Get or set the vector name"""
        return self.name

    @vector_name.setter
    def vector_name(self, name: str) -> None:
        self.name = name

    @property
    def vector_loc(self) -> str:
        """Get or set the vector location"""
        return self.loc

    @vector_loc.setter
    def vector_loc(self, loc: str) -> None:
        self.loc = loc
