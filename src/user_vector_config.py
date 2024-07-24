from base_vector_config import BaseVector

class VectorConfig(BaseVector):

    def vector_name(self, name) -> str:
        self.name = name
        return name
    
    def vector_loc(self, loc) -> str:
        self.loc = loc
        return loc
    
    def set_vector(self, vector_callback, *args):
        result = vector_callback(*args)
        return result