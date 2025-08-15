import streamlit as st

# --- PAGE CONTENT ---
# Main title for the page
st.title(":blue[:material/finance_mode: **SalesSense**]")

# Brief introduction section
# Hero section: headline + subheadline
st.markdown("""
#### :rocket: Turn sales calls into coaching moments

SalesSense gives instant, AI-powered feedback on your Dialpad calls—highlighting what worked, what didn’t, and what to do next.
""")

# Value bullets (ultra-compact)
st.markdown("""
- Spot strengths and blind spots fast
- See sentiment, talk-time, objections, and next steps
- Get actionable, call-specific coaching
""")

# Trust/minimal context line
st.caption("Built on real team calls for relevance. Designed for speed. Perfect for POCs.")

# --- SPACING ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- CENTERED "PROCEED" BUTTON ---
col1, col2, col3 = st.columns([3, 2, 3])  # Centering the button
with col2:
    proceed = st.button(
        label="🚀 Proceed",
        type="primary",
        help="Click to upload your data and get started!",
        use_container_width=True
    )

# --- BUTTON ACTION ---
if proceed:
    st.switch_page("views/upload.py")  # Redirects to Processing Page

# Divider for visual separation
# st.divider()