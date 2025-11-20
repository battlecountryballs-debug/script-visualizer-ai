from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

BACKEND_URL = "http://localhost:8000/process-script"  # backend endpoint

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h2>Script → Video Generator</h2>
    <form method='post' action='/generate'>
        <textarea name='script' rows='10' cols='60' placeholder='Enter your script here...'></textarea>
        <br><br>
        <button type='submit'>Generate Video</button>
    </form>
    """

@app.post("/generate", response_class=HTMLResponse)
async def generate(script: str = Form(...)):
    response = requests.post(BACKEND_URL, json={"script": script})

    if response.status_code != 200:
        return "<h3>Error generating video. Check backend server.</h3>"

    result = response.json()
    return f"""
    <h2>Video Generated!</h2>
    <p>Scenes: {len(result['scenes'])}</p>
    <p>Images: {len(result['images'])}</p>
    <p>Video saved at: {result['video_path']}</p>
    """
