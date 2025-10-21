from pathlib import Path

def write_transcription(text, directory, name, overwrite=False):

    trans_path = Path(directory / name).resolve()

    if trans_path.exists() and not overwrite:
        raise Exception('Transcription file already exists and overwrite is set to false')
    
    directory.mkdir(parents=True, exist_ok=True)
    trans_path.write_text(text)
    

    

