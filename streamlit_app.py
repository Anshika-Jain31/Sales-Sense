import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    layout="wide",
    menu_items={
        'Get Help': f'mailto:{st.secrets["EMAIL"]["ADMIN_EMAIL_ADDRESS"]}',
        'Report a bug': f'mailto:{st.secrets["EMAIL"]["ADMIN_EMAIL_ADDRESS"]}',
        'About': "# Cogent Infotech Innovation Lab"
    }
)

# --- PAGE SETUP ---
# Define app pages using st.Page(), setting titles, icons, and default page.


home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

upload_page = st.Page(
    page="views/upload.py",
    title="Data Ingestion",
    icon=":material/upload:",
)

results_page = st.Page(
    page="views/results.py",
    title="Results",
    icon=":material/insights:",
)

about_us_page = st.Page(
    page="views/about_us.py",
    title="About Us",
    icon=":material/info:",
)


# --- NAVIGATION SETUP ---
# Initialize page navigation to switch between defined pages
navigation = st.navigation(

    # pages=[home_page, processing_page, emr_page, review_page]
    pages={
        "SalesSense": [home_page, upload_page, results_page],
        "Info": [about_us_page]
    },
    # position="top",  # Position of the navigation bar
)

# --- SHARED ON ALL PAGES ---
# Display the company logo at the top of the page
st.logo(
    image="assets/images/cogent_tagline_color.png",  # Main company logo
    icon_image="assets/images/cogent_logo.png"       # Optional icon for the logo
)

# Custom CSS for styling
st.markdown(
    """
    <style>
           .block-container {
                padding-top: 3rem;   /* Adds top padding */
                padding-bottom: 0rem;/* No bottom padding */
                padding-left: 2rem;  /* Adds left padding */
                padding-right: 2rem; /* Adds right padding */
            }
    </style>
    """,
    unsafe_allow_html=True
)

# TODO: Add user login/logout buttons
# ---USER LOGIN/LOGOUT BUTTONS---
# col1, col2 = st.columns([7, 1])

# with col2:
#     st.button("Logout",)

# --- RUN NAVIGATION ---
navigation.run()
