#from vector_class import vector_func
#from embedder import Embedder
from chunking import splitter

# # Usage
# vector_instance = vector_func()
# ch = vector_instance.db_create()
for chunk in splitter():
    print("current chunk:\n")
    print(chunk)