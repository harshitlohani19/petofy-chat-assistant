import os
import sys
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv
from src.client import client_env
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from src.pathmaker import env_path

client = client_env()
# Load environment variables from the .env file
env_path = find_dotenv("config/.env")
load_dotenv(env_path)

service_endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_RESOURCE_KEY")
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
            "content": "what is petofy",
        },
    ],
    extra_body={
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": service_endpoint,
                    "index_name": "petofy-vector-data",
                    "authentication": {
                        "type": "api_key",
                        "key": key,
                    },
                },
            }
        ],
    },
)

print(completion.choices[0].message.content)
