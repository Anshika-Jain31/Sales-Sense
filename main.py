# main.py
from service.assemblyai_test import transcribe_audio

FILE_URL = r"data/dialpad_sample_voice_recordings/Afreen Ali (314) 497-8431 Aug 5, 2025.mp3"

transcript = transcribe_audio(FILE_URL)

print("\n--- Conversation Transcript ---\n")
for utt in transcript.utterances:
    print(f"[{utt.start/1000:.2f}s - {utt.end/1000:.2f}s] Speaker {utt.speaker}: {utt.text}")
