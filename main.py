from pathlib import Path
from argparse import ArgumentParser
from transcribe import transcribe_audio
from write_transcription import write_transcription
from create_speakers import create_speakers


def main():

    parser = ArgumentParser()
    parser.add_argument("audio_file")
    parser.add_argument("speaker_samples")

    args = parser.parse_args()
    audio_path = Path(args.audio_file).resolve()
    samples_path = Path(args.speaker_samples).resolve()

    speakers_info = create_speakers(samples_path)

    text = transcribe_audio(audio_path, speakers_info)

    directory = Path("transcriptions").resolve()
    name = f"{audio_path.stem}_transcription.txt"
    write_transcription(text, directory, name, overwrite=True)


if __name__ == "__main__":
    main()
