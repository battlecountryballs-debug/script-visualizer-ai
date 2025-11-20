from fastapi import FastAPI
from scene_splitter import split_into_scenes
from prompt_generator import generate_prompt
from image_generator import generate_image
from video_maker import make_video

app = FastAPI()

@app.post("/process_script")
async def process_script(data: dict):
    script = data["script"]
    
    scenes = split_into_scenes(script)
    prompts = [generate_prompt(s) for s in scenes]
    images = [generate_image(p) for p in prompts]
    
    video_path = make_video(images)

    return {
        "scenes": scenes,
        "prompts": prompts,
        "images": images,
        "video": video_path
    }
