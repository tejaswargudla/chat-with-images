from dotenv import dotenv_values
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from .image_desc import get_image_desc
from .image_details import get_metadata
from .embeddings import get_embeddings
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

def main():
    list_of_documents = []
    for filename in os.listdir(cfg.get("path")):
        filepath = cfg["path"] + filename
        image_desc = get_image_desc(filepath)
        image_date = get_metadata(filepath)
        if image_date:
            image_desc = image_desc + image_date
        list_of_documents.append(Document(page_content=image_desc, 
                                          metadata=dict(imagepath=filepath)))

    if list_of_documents:
        embedding_model = get_embeddings()
        if embedding_model:
            db = FAISS.from_documents(list_of_documents, embedding_model)
            db.save_local(cfg["embedding_path"])
        else:
            print("Download the embedding model from ollama.")
    else:
        print("No data to preprocess.")
        

if __name__ == "__main__":
    main()
    