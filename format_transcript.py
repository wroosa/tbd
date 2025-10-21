def format_transcript(response):

    lines = []

    for segment in response["segments"]:
        speaker = segment["speaker"]
        text = segment["text"]
        lines.append(f"{speaker}: {text}")
    transcript = "\n".join(lines)

    return transcript
