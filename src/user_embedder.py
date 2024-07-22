from embedder import Embedder

class User_embedding(Embedder):

    def sentence_transformers(self):
        pass
    def hugging_face(self):
        pass
    def azure_embeddings(self):
        pass

    def custom_embedder(self):
        pass

    def set_embedder(self,embedder_callback,):
        result = embedder_callback()
        return result
