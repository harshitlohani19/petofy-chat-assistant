from vector import Vector

vectors=Vector()

class User_vector(Vector):

    def vector_name(self, name):
        return name
    
    def vector_loc(self, loc):
        return loc
    
    def set_vector(self,vector_callback):
        result = vector_callback()
        return result