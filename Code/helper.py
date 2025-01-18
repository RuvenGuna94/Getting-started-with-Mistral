import os
from dotenv import load_dotenv, find_dotenv     

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage



api_key = "ePMByfktIUoCrdndNwwmbY1e8c9mzq8h"
client = None

def load_env():
    _ = load_dotenv(find_dotenv())

def mistral(user_message, 
            model="mistral-small-latest",
            is_json=False):
    
    # client = MistralClient(api_key=api_key, endpoint=dlai_endpoint)
    #client = MistralClient(api_key=api_key)
    #messages = [ChatMessage(role="user", content=user_message)]

   # messages = [
   #     {
   #         "role": "user",
   #         "content": user_message,
    #    },
   # ]



    api_key = "ePMByfktIUoCrdndNwwmbY1e8c9mzq8h"
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    if is_json:
        chat_response = client.chat(
        model= model,
        response_format={"type": "json_object"},
        messages = [
            {
                "role": "user",
                "content": user_message,
            },
        ]
    )
    else:
        chat_response = client.chat(
        model= model,
        messages = [
            {
                "role": "user",
                "content": user_message,
            },
        ]
    )

    return chat_response.choices[0].message.content


def get_text_embedding(txt):
    global client
    embeddings_batch_response = client.embeddings(
        model="mistral-embed", 
        input=txt
    )
    return embeddings_batch_response.data[0].embedding

import requests
from bs4 import BeautifulSoup
import re

def get_web_article_text(url, file_save_name=None):

    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    
    tag = soup.find("div", re.compile("^prose--styled"))
    text = tag.text
    
    if file_save_name:
        f = open(file_save_name, "w")
        f.write(text)
        f.close()
    return text