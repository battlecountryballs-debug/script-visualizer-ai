def split_into_scenes(script: str):
    # Simple scene splitting based on empty lines or "Scene" keyword
    lines = script.split("\n")
    scenes = []
    current = []

    for line in lines:
        if line.strip().lower().startswith("scene") or line.strip() == "":
            if current:
                scenes.append("\n".join(current))
                current = []
        else:
            current.append(line)

    if current:
        scenes.append("\n".join(current))

    return scenes
