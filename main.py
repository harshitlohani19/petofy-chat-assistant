import os
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
from src.pathmaker import env_path

# Load environment variables from the .env file
env_path = find_dotenv("config/.env")
load_dotenv(env_path)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": "What are my available health plans?",
        },
    ],
    extra_body={
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": os.getenv["AZURE_ENDPOINT"],
                    "index_name": "petofy_vector_data",
                    "authentication": {
                        "type": "api_key",
                        "key": os.getenv["AZURE_RESOURCE_KEY"],
                    },
                },
            }
        ],
    },
)

print(completion.model_dump_json(indent=2))
