from base_vector import BaseVector

class VectorConfig(BaseVector):
    def __init__(self):
        super().__init__()

    def set_vector(self, vector_callback, *args):
        result = vector_callback(*args)
        return result
