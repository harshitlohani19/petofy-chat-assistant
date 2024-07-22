from vector import BaseVector

class User_vector(BaseVector):

    def vector_name(self, name):
        return name
    
    def vector_loc(self, loc):
        return loc
    
    def set_vector(self,vector_callback,*args):
        result = vector_callback(*args)
        return result