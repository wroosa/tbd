from pathlib import Path
from openai import OpenAI
from get_openai_client import get_openai_client
from constants import SUPPORTED_CONTEXT_FILE_TYPES


def create_context_files(path):

    client = get_openai_client()

    if not path.is_dir():
        raise Exception(f"Error: Path to context files ({path}) is not a directory")

    context_files = Path(path).iterdir()

    file_objects = []
    for file in context_files:
        if file.is_file():
            ext = file.suffix

            # Check if the type is supported and it's under 10 seconds
            if ext not in SUPPORTED_CONTEXT_FILE_TYPES:
                raise Exception(
                    f"Error: Context file:{file} is an unsupported type {ext}"
                )

            # TODO: Add check for file size limits

            file_objects.append(
                client.files.create(file=open(file, "rb"), purpose="user_data")
            )

    if file_objects == []:
        print("Warning: No context files were found")

    return file_objects
