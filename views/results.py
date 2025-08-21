import streamlit as st

st.title("Results")

if "transcript" not in st.session_state:
    st.warning("⚠️ No transcript found. Please upload and analyze a call first.")
    st.stop()

transcript = st.session_state.transcript

st.subheader("📜 Conversation Transcript")

# Show each speaker's part
for utt in transcript.utterances:
    start = utt.start / 1000
    end = utt.end / 1000
    st.markdown(
        f"<div style='padding:8px; margin:4px; border-radius:8px; background:#f6f6f6'>"
        f"<b>Speaker {utt.speaker}</b> [{start:.2f}s - {end:.2f}s]:<br>{utt.text}"
        f"</div>",
        unsafe_allow_html=True
    )
