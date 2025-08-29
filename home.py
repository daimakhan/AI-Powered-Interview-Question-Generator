# Home.py
import streamlit as st

st.set_page_config(page_title="AI Interview Generator", layout="centered")

if "field" not in st.session_state:
    st.session_state.field = None
if "level" not in st.session_state:
    st.session_state.level = None
if "page" not in st.session_state:
    st.session_state.page = "field"  # default page

# --- PAGE 1: FIELD SELECTION ---
if st.session_state.page == "field":
    st.title("Select Your Field")
    field = st.radio("Choose a field:", ["Artificial Intelligence", "Web Development", "Game Development"])
    if st.button("Done"):
        st.session_state.field = field
        st.session_state.page = "experience"
        st.experimental_rerun()

# --- PAGE 2: EXPERIENCE LEVEL ---
elif st.session_state.page == "experience":
    st.title("Select Experience Level")
    level = st.radio("Choose level:", ["Fresher Intern", "Experienced Intern"])
    if st.button("Done"):
        st.session_state.level = level
        st.session_state.page = "interview"
        st.experimental_rerun()

# --- PAGE 3: INTERVIEW ---
elif st.session_state.page == "interview":
    from pages.Interview import run_interview
    run_interview()
