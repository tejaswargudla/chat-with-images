import ollama

def get_image_desc(imagepath):
    try:
        ollama_op = ollama.generate(
            model="llava",
            prompt="Please describe whats in this image",
            images=[imagepath]
        )
        return ollama_op.get("response", "")
    except Exception as exce:
        return False