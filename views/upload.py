import streamlit as st

# st.set_page_config(page_title="Upload Call | SalesSense", page_icon="🎧", layout="centered")

# Page header
st.markdown("### 🎧 Upload Dialpad Call")
st.caption("Provide the recording and a bit of context so SalesSense can generate accurate, actionable insights.")

# Persistent state for downstream pages
if "upload_ready" not in st.session_state:
    st.session_state.upload_ready = False

with st.form("upload_form", clear_on_submit=False):
    # 1) Audio upload
    audio_file = st.file_uploader(
        label="Dialpad Call Recording",
        type=["mp3", "wav", "m4a", "aac"],
        help=(
            "Upload the audio file from your Dialpad call. "
            "We transcribe this to analyze sentiment, talk-time, objections, and more. "
            "Supported formats: MP3, WAV, M4A, AAC."
        ),
        accept_multiple_files=False
    )

    # 2) Call participants
    participants = st.text_area(
        label="Call Participants (names and roles)",
        placeholder="John Smith (Sales Rep), Sarah Johnson (Prospect), Mike Davis (Prospect's Manager)",
        help=(
            "List everyone on the call with roles. "
            "Why: Roles help tailor feedback (e.g., prospect vs. manager) and improve speaker attribution."
        ),
        height=100
    )

    # 3) Call details & context
    details = st.text_area(
        label="Call Details & Context",
        placeholder="Product demo call for CRM software — discussed pricing and implementation timeline — prospect interested, follow-up scheduled.",
        help=(
            "Briefly describe the purpose, topics discussed, and outcome. "
            "Why: Context sharpens analysis (e.g., a demo vs. negotiation needs different coaching)."
        ),
        height=120
    )

    # 4) Call type (multiselect)
    call_types = st.multiselect(
        label="Call Type",
        options=["Prospecting", "Demo", "Follow-Up", "Negotiation", "Closing", "Customer Support", "Other"],
        help=(
            "Select one or more types that best describe this call. "
            "Why: Call type guides which AI agents weigh in more (e.g., discovery vs. objection handling)."
        ),
        default=[]
    )

    # Inline info for good data hygiene
    with st.expander("Tips for better insights"):
        st.markdown(
            "- Prefer clear audio; avoid heavy background noise.\n"
            "- Use accurate roles for participants (e.g., Decision Maker, Champion).\n"
            "- Add concise context (goal, key topics, outcome) for more targeted coaching.\n"
            "- If sensitive data exists, consider anonymizing names before upload."
        )
    col1, col2, col3 = st.columns([2, 3, 2])

    with col2:
        submitted = st.form_submit_button("Analyze Call", type="primary", use_container_width=True)

# Validation and state handling
if submitted:
    errors = []
    if not audio_file:
        errors.append("Please upload a call recording.")
    if not participants.strip():
        errors.append("Please provide call participants and roles.")
    if not details.strip():
        errors.append("Please provide call details and context.")
    if not call_types:
        errors.append("Please select at least one call type.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        # Preview basic file info
        st.success("Inputs received. Preparing your analysis...")
        st.write(f"• File name: {audio_file.name}")
        st.write(f"• File size: ~{round(len(audio_file.getbuffer())/1024, 2)} KB")
        st.write(f"• Call type(s): {', '.join(call_types)}")

        # Save to session for downstream processing page
        st.session_state.upload_ready = True
        st.session_state.audio_file = audio_file
        st.session_state.participants = participants.strip()
        st.session_state.details = details.strip()
        st.session_state.call_types = call_types


        # Navigate to result page
        st.switch_page("views/results.py")

# Optional: show a subtle note if nothing submitted yet
if not submitted:
    st.caption("All fields are required for best results. Your audio is processed securely for transcription and analysis.")
