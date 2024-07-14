import ollama

def get_embeddings(prompt):
    try:
        embeddings = ollama.embeddings(
            model='nomic-embed-text',
            prompt = prompt
        )
        return embeddings
    except Exception as exce:
        return False