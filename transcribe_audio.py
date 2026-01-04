from openai import OpenAI
from dotenv import load_dotenv
from get_openai_client import get_openai_client
from format_transcript import format_transcript
from pathlib import Path
import json
import os


def transcribe_audio(audio_file, speakers_info):
    
    client = get_openai_client()
    prompt = """
        This is a dungeons and dragons session with 3 players matt playing saladin, walter playing perun and nick playing ako. The dungeon master is isaac who will be speakign as different npcs. Each audio segement is from one continuous session.
    """

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
    ex_file = Path("recent_response.json").resolve()
    ex_file.write_text(response.model_dump_json())

    transcript = format_transcript(json_dict)

    return transcript
