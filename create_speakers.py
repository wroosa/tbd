from pathlib import Path
from pydub import AudioSegment
import base64
from constants import (
    SUPPORTED_AUDIO_FILE_TYPES,
    SPEAKER_SAMPLE_LIMIT,
    SUPPORTED_AUDIO_MIME_TYPES,
)


def create_speakers(path):

    if not path.is_dir():
        raise Exception(
            f"Error: Path to speaker samples ({samples}) is not a directory"
        )

    samples = Path(path).iterdir()

    speakers_names = []
    speaker_samples = []

    for sample in samples:
        if sample.is_file():
            ext = sample.suffix

            # Check if the type is supported and it's under 10 seconds
            if ext not in SUPPORTED_AUDIO_FILE_TYPES:
                raise Exception(
                    f"Error: Speaker sample file:{sample} is an unsupported type {ext}"
                )
            if not length_under_ten(sample):
                raise Exception(
                    f"Error: Speaker sample audio:{sample} is above the length limit of {SPEAKER_SAMPLE_LIMIT} seconds."
                )

            speakers_names.append(sample.stem)
            sample_data_url = create_data_url(sample)
            speaker_samples.append(sample_data_url)

    speakers = {
        "known_speaker_names": speakers_names,
        "known_speaker_references": speaker_samples,
    }

    if speaker_samples == [] or speaker_samples == []:
        print("Warning: No known speakers were found")

    return speakers


def length_under_ten(path_to_audio):
    audio = AudioSegment.from_file(path_to_audio)
    duration_sec = len(audio) / 1000
    return duration_sec <= SPEAKER_SAMPLE_LIMIT


def create_data_url(path):
    with open(path, "rb") as f:
        b64_audio = base64.b64encode(f.read()).decode("utf-8")
    mime = SUPPORTED_AUDIO_MIME_TYPES[path.suffix]
    data_url = f"data:{mime};base64,{b64_audio}"
    return data_url
