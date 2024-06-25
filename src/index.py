from vector.py import load_documents, generate_embeddings
from query import query_documents
from config.env_setup import (
    search_index_client,
    search_client,
    DOCUMENTS_PATH,
    INDEX_NAME,
)


def create_index():
    """Create the index in Azure Cognitive Search."""
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SimpleField(name="content", type=SearchFieldDataType.String),
        SimpleField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        ),
    ]
    index = SearchIndex(name=INDEX_NAME, fields=fields)
    search_index_client.create_index(index)


def index_documents(documents, embeddings):
    """Index the documents and their embeddings in Azure Cognitive Search."""
    batch = IndexDocumentsBatch()
    for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
        batch.add_upload_action(
            {
                "id": str(i),
                "content": doc,
                "embedding": embedding.tolist(),  # Convert numpy array to list
            }
        )
    results = search_client.index_documents(batch)
    for result in results:
        if not result.succeeded:
            print(f"Failed to index document ID {result.key}: {result.error_message}")


if __name__ == "__main__":
    # Load and embed documents
    documents = load_documents(DOCUMENTS_PATH)
    document_embeddings = generate_embeddings(documents)

    # Create index in Azure Cognitive Search
    create_index()

    # Index documents and their embeddings
    index_documents(documents, document_embeddings)

    # Example query
    results = query_documents("example query text")
    for result in results:
        print(f"Document ID: {result['id']}, Content: {result['content']}")
s
