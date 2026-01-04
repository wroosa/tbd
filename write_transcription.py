from pathlib import Path


def write_transcription(text, directory, name, overwrite=False):

    trans_path = Path(directory / name).resolve()

    if trans_path.exists() and not overwrite:
        raise Exception(
            "Transcription file already exists and overwrite is set to false"
        )

    directory.mkdir(parents=True, exist_ok=True)
    trans_path.write_text(text)
    print(f"Transcription complete! Written to: {trans_path}")

def write_summary(text, directory, name, overwrite=False):

    summary_path = Path(directory / name).resolve()

    if summary_path.exists() and not overwrite:
        raise Exception(
            "Summary file already exists and overwrite is set to false"
        )

    directory.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(text)
    print(f"Summary complete! Written to: {summary_path}")