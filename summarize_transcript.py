from get_openai_client import get_openai_client
from format_transcript import format_transcript
from pathlib import Path
from constants import CHUNK_TOKEN_MAX
import re
import tiktoken


def generate_summary(transcript, context_files, previous_summaries):
    client = get_openai_client()
    model_input = create_input(transcript, context_files + previous_summaries)

    return generate(client, model_input)


def generate(client, model_input):
    system_prompt = """
        You are an expert and experienced dungeon master who is creating a session summary based on a audio transcript that is provided. You will also have all previously generated session summaries to reference and some documents that contain context about the world and things within it. Using all of this information create a session summary with chronological events and key moments/decisions as well as characters we met.
    """
    response = client.responses.create(
        model="gpt-5",
        input=model_input,
        instructions=system_prompt,
    )
    return response.output_text


def create_input(transcript, files):

    content = [
        {
            "type": "input_text",
            "text": transcript,
        }
    ]

    for file in files:
        content.append({"type": "input_file", "file_id": file.id})

    return [
        {"role": "user", "content": content},
    ]


###### Unused code for splitting transcript into chunks based on token count ######

# def split_transcript(transcript):
#     # TODO: Perhaps there is a better way of splitting that preserves a scenes integrity. Being able to identify when there is a pause or transition of location.
#     delimiter = r"(.)"
#     text_pieces = re.split(delimiter, transcript)
#     sentences = []
#     for text in text_pieces:
#         count = get_token_count(text)
#         sentences.append([text, count])
#     # Add lines to chunk until above max or no lines remain
#     # TODO double while loop is not ideal and I should really do this using encoded chunks - need to refactor this is nasty
#     chunks = []
#     i = 0
#     num_sentences = len(sentences)
#     chunk_sum = 0
#     temp_chunk = ''
#     while chunk_sum < CHUNK_TOKEN_MAX and i < num_sentences:
#         temp_chunk+=

# def get_token_count(text):
#     # TODO add model argument and model to options/constants
#     encoding = tiktoken.get_encoding("o200k_base")
#     num_tokens = len(encoding.encode(text))
#     return num_tokens
