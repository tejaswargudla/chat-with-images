import ollama
import os
import sys
from dotenv import dotenv_values

path = os.getcwd()
if "/chat-with-images" in path:
    path = path.rsplit("/chat-with-images", 1)[0]
    path = path + "/chat-with-images"
    if path not in sys.path:
        sys.path.insert(0, path)
    cfg = dotenv_values(f'{path}/.env')
else:
    cfg = dotenv_values(".env")

def get_image_desc(imagepath):
    try:
        ollama_op = ollama.generate(
            model=cfg.get("mutlimodal_model"),
            prompt="Please describe whats in this image",
            images=[imagepath]
        )
        return ollama_op.get("response", "")
    except Exception as exce:
        return False