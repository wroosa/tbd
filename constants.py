SUPPORTED_AUDIO_FILE_TYPES = (
    ".flac",
    ".mp3",
    ".mp4",
    ".mpeg",
    ".mpga",
    ".m4a",
    ".ogg",
    ".wav",
    ".webm",
)
SUPPORTED_AUDIO_MIME_TYPES = {
    ".flac": "audio/flac",
    ".mp3": "audio/mpeg",
    ".mp4": "audio/mp4",
    ".mpeg": "audio/mpeg",
    ".mpga": "audio/mpeg",
    ".m4a": "audio/m4a",
    ".ogg": "audio/ogg",
    ".wav": "audio/wav",
    ".webm": "audio/webm",
}
SPEAKER_SAMPLE_LIMIT = 10.0  # Seconds
MB_BYTES = 1048576  # Bytes
BATCH_SIZE_LIMIT = 20.0  # Megabytes
FILE_SIZE_LIMIT = 1000  # Megabytes
BATCH_TIME_SIZE = 180000  # Milisecond
CHUNK_TOKEN_MAX = 5000  # Tokens
