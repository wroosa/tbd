from pydub import AudioSegment
from pathlib import Path
from constants import (
    SUPPORTED_AUDIO_FILE_TYPES,
    MB_BYTES,
    FILE_SIZE_LIMIT,
    BATCH_SIZE_LIMIT,
    BATCH_TIME_SIZE,
)
from transcribe_audio import transcribe_audio
from tempfile import TemporaryDirectory


def transcribe(audio_path, speakers_info):

    path = Path(audio_path).resolve()
    extension = path.suffix
    audio_format = extension.strip(".")
    size_MB = get_file_size_MB(path)
    name = path.stem

    if not path.is_file():
        raise Exception(f"Error: Path to audio file {path} is not a file")

    if extension not in SUPPORTED_AUDIO_FILE_TYPES:
        raise Exception(
            f"Error: Audio file:{path} is an unsupported type {audio_format}"
        )

    if size_MB > FILE_SIZE_LIMIT:
        raise Exception(
            f"Error: Audio file:{path} is above the file size limit of {FILE_SIZE_LIMIT}MB"
        )

    # If the file is above the batch size limit split it and stitch the results for each segement otherwise just transcribe once.
    if size_MB > BATCH_SIZE_LIMIT:
        transcript_chunks = []
        audio = AudioSegment.from_file(path, format=audio_format)
        chunks = audio[::BATCH_TIME_SIZE]

        # Create a temportary directory for the chunked audio files
        with TemporaryDirectory(prefix="transcription_") as tmpdir:
            temp_folder_path = Path(tmpdir)
            print(f"Temp folder: {tmpdir}")

            for i, chunk in enumerate(chunks):
                temp_file_name = f"{name}-temp{i}.{audio_format}"
                temp_file_path = temp_folder_path / temp_file_name
                chunk.export(temp_file_path, format=audio_format)
                print(f"Transcribing chunk {i} temp_file:{temp_file_path}")

                with open(temp_file_path, "rb") as f:
                    # TODO: Implement further batch splitting for large sizes
                    # if get_file_size_MB(temp_name) > BATCH_SIZE_LIMIT:
                    chunk_transcript = transcribe_audio(f, speakers_info)
                    transcript_chunks.append(chunk_transcript)

                # Delete the temporary file after transcription
                temp_file_path.unlink(missing_ok=True)

        # Merge transcript chunks into one transcript
        transcript = "\n".join(transcript_chunks)
    else:
        print(f"Transcribing whole file. File size below batching limit")
        transcript = transcribe_audio(path, speakers_info)

    return transcript


def get_file_size_MB(path):
    path = Path(path)
    size_bytes = path.stat().st_size
    return size_bytes / MB_BYTES
