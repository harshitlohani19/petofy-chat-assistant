import os
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
from chroma import query_db

# Load environment variables
env_path = find_dotenv("config/.env")
load_dotenv(env_path)

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)


while True:
    query = input("Enter your question: ").strip().lower()
    if query == "exit":
        break

    retrieved_texts, _ = query_db(query)
    # Base prompt
    prompt_base = (
        "Based on the following information:"
        f"{retrieved_texts}"
        "Please provide a direct and concise response for the following question and if the information needed to answer the question is not present in the provided text, reply with 'Sorry, I can't answer that.'\n"
    )
    prompt = prompt_base + query

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Only provide responses based on the information given. If asked questions outside the dataset, reply 'Sorry, I can't answer that.'",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    answer = response.choices[0].message.content.strip()
    print("output:", answer)