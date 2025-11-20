def generate_image(prompt: str):
    # Placeholder image URL (Later we will connect to real AI image API)
    safe_prompt = prompt.replace(" ", "+")
    return f"https://dummyimage.com/1024x1024/000/fff&text={safe_prompt}"
