import sys; sys.path.append('..')

import pandas as pd
import streamlit as st
from modules.nav import NavigationBar
from modules.pipes import DisplayPipeExecution
from src.credit_fraud_detector.pipelines.download_feature_store.nodes import download_from_feature_store



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
        DisplayPipeExecution(pipe_tag=pipe_tag)
    with col2:
        fs_df = None
        while not isinstance(fs_df, pd.DataFrame):
            info_box = st.empty()
            info_box.info('Downloading data from Hopsworks')
            fs_df = download_from_feature_store()
        info_box.empty()
        st.dataframe(fs_df)


elif train_button:
    data_button = False
    pipe_tag = 'train'
    with col1:
        DisplayPipeExecution(pipe_tag=pipe_tag)
    with col2:
        st.image('./images/pastel-de-nata.png', caption='PLACEHOLDER FOR RETURN')
