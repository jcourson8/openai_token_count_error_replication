import ast
import os
import openai
import tiktoken

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

with open('documents_list.txt', 'r') as file:
    documents = file.read().strip() 

documents= ast.literal_eval(documents)
encoding = tiktoken.get_encoding("cl100k_base")
num_tokens = sum(len(encoding.encode(doc)) for doc in documents)
print(f"Number of tokens: {num_tokens}")

client = openai.OpenAI(api_key=OPENAI_API_KEY)
response = client.embeddings.create(model="text-embedding-3-large", input=documents)

print(f'Number of total tokens: {response.usage.total_tokens}') 
