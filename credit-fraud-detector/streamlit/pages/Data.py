import os
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Data sources",
    page_icon="./pastel-de-nata.png",
    layout='wide')

st.markdown(
    '''
    # Here you can see our data during different phases of our pipeline.

    Go ahead, try it:
    '''
)

@st.cache_data
def get_data(choice: str):
    choice_map = {
        'Raw': '01_raw',
        'Preprocessed': '03_primary',
        'From feature store': '04_feature'
    }

    df_choice = choice_map[choice]

    path = os.path.join('..', 'data', df_choice)
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)
    csv = files[0]

    data = pd.read_csv(csv)

    return data

choice = st.radio('Select the level:', ('Raw', 'Preprocessed', 'From feature store'))

df = get_data(choice)
st.dataframe(df)
