import os
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def get_data(choice: str) -> pd.DataFrame:
    choice_map = {
        'Raw': '01_raw',
        'Preprocessed': '03_primary',
        'From feature store': '04_feature'
    }

    df_choice = choice_map[choice]

    path = os.path.join('..', 'data', df_choice)
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    csv = files[0]

    data = pd.read_csv(csv)

    return data

def plot_feats(df):
    st.markdown('## Features')

    fig, ax = plt.subplots(2, 2, figsize=(15, 7))

    try:
        amount_val = df['Amount'].values
        time_val = df['Time'].values
    except KeyError:
        amount_val = df['scaled_amount'].values
        time_val = df['scaled_time'].values
    v1 = df['V1'].values
    v2 = df['V2'].values


    sns.distplot(amount_val, ax=ax[0][0], color='r')
    ax[0][0].set_title('Distribution of Transaction Amount', fontsize=14)
    ax[0][0].set_xlim([min(amount_val), max(amount_val)])

    sns.distplot(time_val, ax=ax[0][1], color='b')
    ax[0][1].set_title('Distribution of Transaction Time', fontsize=14)
    ax[0][1].set_xlim([min(time_val), max(time_val)])

    sns.distplot(v1, ax=ax[1][0], color='orange')
    ax[1][0].set_title('V1', fontsize=14)
    ax[1][0].set_xlim([min(v1), max(v1)])

    sns.distplot(v2, ax=ax[1][1], color='green')
    ax[1][1].set_title('V2', fontsize=14)
    ax[1][1].set_xlim([min(v2), max(v2)])

    st.pyplot(fig)