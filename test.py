import os
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv("config/.env")

load_dotenv(env_path)
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
)

response = client.chat.completions.create(
    model="gpt-35-turbo",  # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {
            "role": "assistant",
            "content": "Yes, customer managed keys are supported by Azure OpenAI.",
        },
        {"role": "user", "content": "Do other Azure AI services support this too?"},
    ],
)

print(response.choices[0].message.content)
