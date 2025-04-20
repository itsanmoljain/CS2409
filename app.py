import streamlit as st
from pages.home import home
from pages.predict import predict
st.set_page_config(initial_sidebar_state="collapsed")
# --------------------- Session Setup ---------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------------- Navigation Button ---------------------

if st.session_state.page == "home":
    home()

elif st.session_state.page == "predictor":
    predict()
