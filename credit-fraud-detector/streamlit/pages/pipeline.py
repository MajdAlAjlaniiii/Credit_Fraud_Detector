import os
import requests
import subprocess

import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path
from dotenv import load_dotenv
from kedro.framework.project import configure_project
from modules.nav import NavigationBar

# Page configuration
load_dotenv()

pkg = Path(__file__).parent.name
configure_project(pkg)

if 'kedro_viz_started' not in st.session_state:
    st.session_state['kedro_viz_started'] = False

st.set_page_config(
    page_title="Pipelines",
    page_icon="./images/pastel-de-nata.png",
    layout='wide')

NavigationBar()

# Page content
st.markdown(
    '''
    # Here you can check our pipelines, developed with Kedro.
    '''
)

def run_kedro_viz(reporter):
    if not st.session_state['kedro_viz_started']:
        reporter.warning('Starting server...')

        subprocess.run(['kedro', 'viz', '--no-browser'], cwd='../', capture_output=True, text=True)

        reporter.info('Waiting for server start...')

        resp = requests.get(os.environ.get('KEDRO_VIZ'))
        while not resp and resp.status_code == 200:
            reporter.info('Waiting for server start...')
            print(resp)
            resp = requests.get(os.environ.get('KEDRO_VIZ'))

        st.session_state['kedro_viz_started'] = True
        reporter.empty()


def show_pipeline_viz():
    st.subheader('PIPELINE VISUALIZATION')

    reporter = st.empty()

    run_kedro_viz(reporter)

    if st.session_state['kedro_viz_started']:
        st.caption('This is interactive')
        components.iframe(os.environ.get('KEDRO_VIZ'), width=1400, height=900)


show_pipeline_viz()
