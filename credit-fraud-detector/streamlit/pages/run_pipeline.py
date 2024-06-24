import streamlit as st
import subprocess
from modules.nav import NavigationBar

# Page auxiliary functions
def run_pipeline(pipe_tag):
    command = ['kedro', 'run', '--tags', pipe_tag]
    process = subprocess.Popen(command, cwd='../', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    placeholder = st.empty()
    with placeholder.container(height=250):
        while process.poll() is None:
            line = process.stdout.readline()
            if not line:
                continue
            st.write(line.strip())


# Page configuration
st.set_page_config(
    page_title="Pipelines",
    page_icon="./images/pastel-de-nata.png",
    layout='wide')

NavigationBar()


# Page content
st.markdown(
    '''
    # Here you can run different parts of the pipeline
    Please, choose which part you want to run:
    '''
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('### Data ingestion, preprocessing, feature store')
    if st.toggle('Click me to check the data pipeline'):
        st.image('./images/data_pipeline.png')
    data_button =  st.button('Run this!', key='data')

with col2:
    st.markdown('### Model training, evaluation, logging')
    if st.toggle('Click me to check the train pipeline'):
        st.image('./images/train_pipeline.png')
    train_button = st.button('Run this!', key='train')


if data_button:
    train_button = False
    pipe_tag = 'data'
    with col1:
        run_pipeline(pipe_tag=pipe_tag)
    with col2:
        st.image('./images/pastel-de-nata.png', caption='PLACEHOLDER FOR RETURN')

elif train_button:
    data_button = False
    pipe_tag = 'train'
    with col1:
        run_pipeline(pipe_tag=pipe_tag)
    with col2:
        st.image('./images/pastel-de-nata.png', caption='PLACEHOLDER FOR RETURN')
