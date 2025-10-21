from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from format_transcript import format_transcript
import json
import os


def transcribe_audio(audio_path, speakers_info):
    load_dotenv()
    api_key = os.getenv("OPEN_API_KEY")
    client = OpenAI(api_key=api_key)

    prompt = """
        This is a dungeons and dragons session with 3 players matt playing saladin, walter playing perun and nick playing ako. The dungeon master is isaac who will be speakign as different npcs. Each audio segement is from one continuous session.
    """

    with audio_path.open("rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-transcribe-diarize",
            chunking_strategy="auto",
            extra_body=speakers_info,
            language="en",
            response_format="diarized_json",
        )
    json_dict = response.model_dump()

    # LOAD EXAMPLE FILE TO BYPASS QUERY
    # ex_file = Path("response_example.json").resolve()
    # with ex_file.open("r", encoding="utf-8") as f:
    #     json_dict = json.load(f)

    # WRITE TO AN EXAMPLE FILE
    # ex_file.write_text(data)

    transcript = format_transcript(json_dict)

    return transcript
