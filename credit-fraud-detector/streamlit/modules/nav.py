import streamlit as st

def NavigationBar():
    with st.sidebar:
        st.page_link('index.py', label='Homepage', icon='🪙')
        st.page_link('pages/data.py', label='Check the data', icon='📊')
        st.page_link('pages/pipeline.py', label='Visualize the pipeline', icon='🪠')
        st.page_link('pages/run_pipeline.py', label='Run the pipeline', icon='🪄')
