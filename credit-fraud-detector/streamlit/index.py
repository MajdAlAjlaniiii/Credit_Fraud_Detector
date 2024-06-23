import streamlit as st
from modules.nav import NavigationBar

# Page configuration
st.set_page_config(
    page_title="Dashboard tool",
    page_icon="./images/pastel-de-nata.png")

NavigationBar()

# Page content
st.markdown(
    '''
    # Welcome to our humble dashboard.

    The sidebar on the left allows you to navigate throught different chunks
    of our project.
    '''
)
