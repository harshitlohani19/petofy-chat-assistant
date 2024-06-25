def generate_embeddings(documents):
    client = AzureOpenAI(
        api_key="f398797cbb734cfdb1de68fdc68cae67",
        api_version="2024-02-01",
        azure_endpoint="https://petofy-test.openai.azure.com/",
    )
    for docs in documents:
        print(docs)

        abcd = client.embeddings.create(input=docs, model="text-embedding")
        return abcd


generate_embeddings(documents)
