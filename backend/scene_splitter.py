def split_into_scenes(script: str):
    scenes = script.split(".")
    scenes = [s.strip() for s in scenes if s.strip()]
    return scenes
