from embedder import Embedder

class User_embedding(Embedder):



    def custom_embedder(self):
        pass



    def set_embedder(self,embedder_callback,):
        result = embedder_callback()
        return result
