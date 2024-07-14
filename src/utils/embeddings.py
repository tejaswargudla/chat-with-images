from langchain_community.embeddings import OllamaEmbeddings
from dotenv import dotenv_values
import os
import sys
path = os.getcwd()
if "/chat-with-images" in path:
    path = path.rsplit("/chat-with-images", 1)[0]
    path = path + "/chat-with-images"
    if path not in sys.path:
        sys.path.insert(0, path)
    cfg = dotenv_values(f'{path}/.env')
else:
    cfg = dotenv_values(".env")
    
def get_embeddings():
    try:
        embedding_model = OllamaEmbeddings(
            model=cfg.get("embedding_model"),
        )
        return embedding_model
    except Exception as exce:
        return False