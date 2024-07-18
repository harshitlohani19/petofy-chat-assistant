from sentence_transformers import SentenceTransformer
from chunking import splitter

chunks = splitter()


def st_model():
    model_list = [
        "all - mpnet - base - v2",
        "multi - qa - mpnet - base - dot - v1",
        "all - distilroberta - v1",
        "all - MiniLM - L12 - v2",
        "multi - qa - distilbert - cos - v1",
        "all - MiniLM - L6 - v2",
        "multi - qa - MiniLM - L6 - cos - v1",
        "paraphrase - multilingual - mpnet - base - v2",
        "paraphrase - albert - small - v2",
        "paraphrase - multilingual - MiniLM - L12 - v2",
        "paraphrase - MiniLM - L3 - v2",
        "distiluse - base - multilingual - cased - v1",
        "distiluse - base - multilingual - cased - v2",
    ]
    print("Choose model from:")
    for model in model_list:
        print(model)

    # model_name = input(str("Enter: "))
    model = SentenceTransformer("all - MiniLM - L6 - v2")
    # Load the SentenceTransformer model
    model = SentenceTransformer(model_name)

    # Example of using the model (you can adjust this based on your application)
    sentence_embeddings = model.encode(["Hello, world!", "How are you?"])
    print(sentence_embeddings)


st_model()


st_model()
