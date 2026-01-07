from pathlib import Path
from get_openai_client import get_openai_client
from constants import SUPPORTED_FILE_TYPES


def create_input_files_from_dir(path):

    if not path.is_dir():
        raise Exception(f"Error: Path to input files ({path}) is not a directory")

    client = get_openai_client()

    # Create a dictionary of existing files keyed by the filename
    existing_files = {}
    for f in client.files.list()["data"]:
        existing_files[f["filename"]] = f

    files = Path(path).iterdir()
    file_objects = []
    for file in files:
        if file.is_file():
            ext = file.suffix

            # Check if the type is supported and it's under 10 seconds
            if ext not in SUPPORTED_FILE_TYPES:
                raise Exception(
                    f"Error: Input file:{file} is an unsupported type {ext}"
                )
            # TODO: Add check for file size limits

            # If the file exists with the same name then grab the file object otherwise create it
            file_obj = existing_files.get(file.name, None)

            if file_obj:
                file_objects.append(file_obj)
            else:
                file_objects.append(
                    client.files.create(file=open(file, "rb"), purpose="user_data")
                )

    if file_objects == []:
        print(f"Warning: No input files were found in directory: {path}")

    return file_objects
