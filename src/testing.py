from vector_class import vector_func
from embedder import Embedder

# Usage
vector_instance = vector_func()
ch = vector_instance.db_create()
print(f"Collection created/updated: {ch.name}")
