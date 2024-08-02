from chromadb.utils import embedding_functions
from base_embedder import Embedder
from sentence_transformers import SentenceTransformer
from transformers import AutoModel
import fasttext
import fasttext.util


class sen_transformer_embedder(Embedder):
    def embedder(self):
        # 1. Load a pretrained Sentence Transformer model
        model = SentenceTransformer("all-MiniLM-L12-v2")
        return model


class hugging_face_one(Embedder):
    def embedder(self):
        model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-code', trust_remote_code=True)
        return model


class meta_embedder(Embedder):
    def embedder(self):
        # Download the pre-trained model
        fasttext.util.download_model('en', if_exists='ignore')  # 'en' is the language code for English
        # Load the model
        ft = fasttext.load_model('cc.en.300.bin')
        return ft


class ChromaEmbedder(Embedder):
    def embedder(self):
        emb = embedding_functions.DefaultEmbeddingFunction()
        return emb
