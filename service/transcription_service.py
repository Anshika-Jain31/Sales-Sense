import assemblyai as aai
import os
import tempfile
from dotenv import load_dotenv

# Load API key
load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

def transcribe_audio(audio_file):
    """
    Transcribes an uploaded audio file (Streamlit UploadedFile) 
    using AssemblyAI with speaker labels.
    Returns the transcript object.
    """
    # 1. Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # 2. Config with speaker labels
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        format_text=True,
        punctuate=True,
        speech_model=aai.SpeechModel.best,
        language_detection=True
    )

    # 3. Run transcription
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(tmp_path)

    # 4. Handle errors
    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(transcript.error)

    return transcript
