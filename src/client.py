import os
import openai
from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI

# Load environment variables from the .env file
env_path = find_dotenv("config/.env")
load_dotenv(env_path)


def client_env():
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-01",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
    # print(client)
    return client


client_env()
