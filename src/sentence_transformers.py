from sentence_transformers import SentenceTransformer

chunks = splitter()

def st_model():
    model_list = [
        "all-mpnet-base-v2",
        "multi-qa-mpnet-base-dot-v1",
        "all-distilroberta-v1",
        "all-MiniLM-L12-v2",
        "multi-qa-distilbert-cos-v1",
        "all-MiniLM-L6-v2",
        "multi-qa-MiniLM-L6-cos-v1",
        "paraphrase-multilingual-mpnet-base-v2",
        "paraphrase-albert-small-v2",
        "paraphrase-multilingual-MiniLM-L12-v2",
        "paraphrase-MiniLM-L3-v2",
        "distiluse-base-multilingual-cased-v1",
        "distiluse-base-multilingual-cased-v2",
    ]
    print("Choose model from:")
    for i, model in enumerate(model_list, 1):
        print(f"{i}. {model}")
    
    choice = input("Enter the number or name of the model you want to use: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(model_list):
        name = model_list[int(choice) - 1]
    elif choice in model_list:
        name = choice
    else:
        print("Invalid input. Using default model.")
        name = "all-MiniLM-L6-v2"  # Default model

    print(f"Loading model: {name}")
    model = SentenceTransformer(name)
    
    all_embeddings = []
    for chunk in chunks:
        embeddings = model.encode(chunk)
        all_embeddings.append(embeddings)
    
    print("Embeddings generated for all chunks")
    return all_embeddings

embeddings = st_model()