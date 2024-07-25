import chromadb
from base_storage import BaseStorage
from user_splitter import ChunkSplitter
from loader import load_json

combined_data, data = load_json()


class VectorDB(BaseStorage):
    # def __init__(self):
    splitter_instance = ChunkSplitter()

    def db_creation(self, splitter_instance, db_name: str, dbloc: str, emb_fun) -> None:
        client = chromadb.PersistentClient(path=f"{dbloc}")
        split_results = splitter_instance.set_splitter(splitter_instance.splitter, data)

                # Check if the collection already exists
        existing_collections = client.list_collections()
        collection_names = [col.name for col in existing_collections]
        
        if db_name in collection_names:

            # Prompt user if they want to update the existing collection
            choice = input(f"The collection '{db_name}' already exists. Do you want to update it? (yes/no): ").strip().lower()
            if choice == 'no':
                print("Exiting without updating.")
                collection = client.get_collection(name=db_name)
                return collection
            
            elif choice == 'yes':
                print("Updating the existing collection.")
                collection = client.get_collection(name=db_name)
                for chunk, chunk_id in split_results:
                    collection.add(documents=chunk, ids=chunk_id)
                print("Updated")
                return collection
        else:
            # Create a new collection if it does not exist
            print("Creating a new collection.")
            collection = client.create_collection(
                name=db_name, embedding_function=emb_fun
            )
            # Add new chunks to the collection
            for chunk, chunk_id in split_results:
                collection.add(documents=chunk, ids=chunk_id)

            print("success.")
            return collection

    def set_database(self, splitter, db_name: str, dbloc: str, emb_fun, callback):
        return callback(splitter, db_name, dbloc, emb_fun)




# class VectorDB(BaseStorage):
#     def __init__(self):
#         self.splitter_instance = ChunkSplitter()

#     def db_creation(self, splitter_instance, db_name: str, dbloc: str, emb_fun) -> None:
#         client = chromadb.PersistentClient(path=f"{dbloc}")

#         split_results = splitter_instance.set_splitter(splitter_instance.splitter, data)

#         existing_collections = client.list_collections()
#         collection_names = [col.name for col in existing_collections]

#         if db_name in collection_names:
#             choice = input(f"The collection '{db_name}' already exists. Do you want to update it? (yes/no): ").strip().lower()
#             if choice == 'no':
#                 print("Exiting without updating.")
#                 collection = client.get_collection(name=db_name)
#                 return collection
            
#             elif choice == 'yes':
#                 print("Updating the existing collection.")
#                 collection = client.get_collection(name=db_name)
#                 for chunk, chunk_id in split_results:
#                     collection.add(documents=chunk, ids=chunk_id)
#                 print("Updated")
#                 return collection
            
#         else:
#             print("Creating a new collection.")
#             collection = client.create_collection(
#                 name=db_name, embedding_function=emb_fun
#             )
#             for chunk, chunk_id in split_results:
#                 collection.add(documents=chunk, ids=chunk_id)
#             print("Success.")
#             return collection

#     def set_database(self, splitter, db_name: str, dbloc: str, emb_fun, callback):
#         result = callback(splitter, db_name, dbloc, emb_fun)
#         return result










# import chromadb
# from base_storage import BaseStorage
# from user_splitter import ChunkSplitter
# from loader import load_json

# combined_data, data = load_json()

# class VectorDB(BaseStorage):
#     def __init__(self):
#         self.splitter_instance = ChunkSplitter()

#     def db_creation(self, splitter_instance, db_name: str, dbloc: str, emb_fun) -> None:
#         client = chromadb.PersistentClient(path=f"{dbloc}")

#         split_results = splitter_instance.set_splitter(splitter_instance.splitter, data)

#         existing_collections = client.list_collections()
#         collection_names = [col.name for col in existing_collections]

#         if db_name in collection_names:
#             choice = input(f"The collection '{db_name}' already exists. Do you want to update it? (yes/no): ").strip().lower()
#             if choice == 'no':
#                 print("Exiting without updating.")
#                 collection = client.get_collection(name=db_name)
#                 return collection
            
#             elif choice == 'yes':
#                 print("Updating the existing collection.")
#                 collection = client.get_collection(name=db_name)
#                 for chunk, chunk_id in split_results:
#                     collection.add(documents=chunk, ids=chunk_id)
#                 print("Updated")
#                 return collection
#         else:
#             print("Creating a new collection.")
#             collection = client.create_collection(
#                 name=db_name, embedding_function=emb_fun
#             )
#             for chunk, chunk_id in split_results:
#                 collection.add(documents=chunk, ids=chunk_id)
#             print("Success.")
#             return collection

#     def set_database(self, splitter, db_name: str, dbloc: str, emb_fun, callback):
#         result = callback(splitter, db_name, dbloc, emb_fun)
#         return result


# import chromadb
# from base_storage import Basestorage
# from user_splitter import UserSplitAlgo
# from loader import load_json

# combined_data, data = load_json()

# class VectorDB(Basestorage):
    
#     splitter = UserSplitAlgo()

#     def db_creation(self, splitter, db_name, dbloc, emb_fun):
#         client = chromadb.PersistentClient(path=f"{dbloc}")

#         split_results = splitter.set_splitter(splitter.custom_splitter, data)

#         # Check if the collection already exists
#         existing_collections = client.list_collections()
#         collection_names = [col.name for col in existing_collections]
        
#         if db_name in collection_names:

#             # Prompt user if they want to update the existing collection
#             choice = input(f"The collection '{db_name}' already exists. Do you want to update it? (yes/no): ").strip().lower()
#             if choice == 'no':
#                 print("Exiting without updating.")
#                 collection = client.get_collection(name=db_name)
#                 return collection
            
#             elif choice == 'yes':
#                 print("Updating the existing collection.")
#                 collection = client.get_collection(name=db_name)
#                 for chunk, chunk_id in split_results:
#                     collection.add(documents=chunk, ids=chunk_id)
#                 print("Updated")
#                 return collection
#         else:
#             # Create a new collection if it does not exist
#             print("Creating a new collection.")
#             collection = client.create_collection(
#                 name=db_name, embedding_function=emb_fun
#             )
#             # Add new chunks to the collection
#             for chunk, chunk_id in split_results:
#                 collection.add(documents=chunk, ids=chunk_id)

#             print("success.")
#             return collection
    
#     def set_database(self, splitter, db_name, dbloc, emb_fun, callback):
#         result = callback(splitter, db_name, dbloc, emb_fun)
#         return result
