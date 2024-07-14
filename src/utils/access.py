from langchain_community.vectorstores import FAISS
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

def is_exists():
    if os.path.exists(cfg.get("embedding_path")):
        files = os.listdir(cfg.get("embedding_path"))
        if ("index.faiss" not in files) and ("index.pkl" not in files):
            return False
        else:
            return True
    else:
        return False
        