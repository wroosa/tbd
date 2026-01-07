from pathlib import Path
from argparse import ArgumentParser
from transcribe_audio import transcribe_audio
from write_transcription import write_transcription, write_summary
from create_speakers import create_speakers
from transcribe import transcribe
from summarize_transcript import generate_summary
from create_input_files import create_input_files_from_dir


def main():

    parser = ArgumentParser()
    parser.add_argument("audio_file")
    parser.add_argument("speaker_samples")

    args = parser.parse_args()
    audio_path = Path(args.audio_file).resolve()
    samples_path = Path(args.speaker_samples).resolve()
    context_path = Path("context_files/")
    summaries_path = Path("session_summaries/")

    context_files = create_input_files_from_dir(context_path)
    summary_files = create_input_files_from_dir(summaries_path)

    # speakers_info = create_speakers(samples_path)

    # text = transcribe(audio_path, speakers_info)

    ##### Get text from file to bypass transcription
    with open("transcriptions/full_transcription.txt", "r") as file:
        text = file.read()

    # transciption_directory = Path("transcriptions").resolve()
    # name = f"{audio_path.stem}_transcription.txt"
    # write_transcription(text, transciption_directory, name, overwrite=True)
    summary = generate_summary(text, context_files, summary_files)

    summary_directory = Path("session_summaries").resolve()
    name = f"{audio_path.stem}_summary.txt"
    write_summary(summary, summary_directory, name, overwrite=True)


if __name__ == "__main__":
    main()
