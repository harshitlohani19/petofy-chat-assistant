import logging
import chromadb
from chromadb.utils import embedding_functions
from loader import load_json
from embedder import Embedder

# Set logging level to ERROR to suppress INFO messages
logging.getLogger("chromadb").setLevel(logging.ERROR)
query_text = ""

embedder = Embedder().model_name


def db_create():
    combined_data = load_json()

    client = chromadb.PersistentClient(
        path="/home/harshitlohani/Desktop/Projects/petofy-chat-assistant/chromadb/"
    )

    embf = embedder  # by default all-MiniLM-L6-v2
    documents = []
    # Combine Prompt and Response into a single document
    for item in combined_data:
        for key, value in item.items():
            documents.append(value)

    # Generate unique IDs for each document
    ids = [f"doc{i+1}" for i in range(len(documents))]

    collection = client.get_or_create_collection(name="vbd", embedding_function=embf)

    collection.add(documents=documents, ids=ids)

    collection = client.get_collection(name="vbd", embedding_function=embf)

    data = collection.peek()["embeddings"]

    return collection


# db_create()


def query_db(query_text):

    client = chromadb.PersistentClient(
        path="/home/harshitlohani/Desktop/Projects/petofy-chat-assistant/chromadb/"
    )
    embf = embedding_functions.DefaultEmbeddingFunction()  # by default all-MiniLM-L6-v2

    collection = client.get_collection(name="vbd", embedding_function=embf)
    # Perform a similarity search
    # query_text = input(str("Enter query"))
    # query_text = "what is a petofy"
    results = collection.query(
        query_texts=[query_text], n_results=5, include=["documents", "distances"]
    )

    documents = results["documents"]
    # print(documents)
    s = ""
    for doc in documents:
        for i in doc:
            s = s + i
    # print(results)
    return s, query_text


query_db(query_text)
