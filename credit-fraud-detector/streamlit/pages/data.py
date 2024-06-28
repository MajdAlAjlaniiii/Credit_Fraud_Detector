import os
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from modules.nav import NavigationBar

# Page configuration
st.set_page_config(
    page_title="Data sources",
    page_icon="./images/pastel-de-nata.png",
    layout='wide')

NavigationBar()

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


# Page content
st.markdown(
    '''
    # Here you can see our data during different phases of our pipeline.

    Go ahead, try it:
    '''
)

# Choose data
choice = st.radio('Select the level:', ('Raw', 'Preprocessed', 'From feature store'))

# Get and show the data as table
df = get_data(choice)
st.dataframe(df.head(5))

# Visualization of Class
st.markdown('## Class')

fig, ax = plt.subplots(figsize=(15, 7))
sns.countplot(x='Class', data=df, ax=ax, palette=['blue', 'red'])
ax.set_title('Class Distributions \n (0: No Fraud || 1: Fraud)', fontsize=14)
for p in ax.patches:
    x = p.get_bbox().get_points()[:,0]
    y = p.get_bbox().get_points()[1,1]
    ax.annotate(f'{100.*y/df.shape[0]:.2f}%', (x.mean(), y),
            ha='center', va='bottom')

st.pyplot(fig)

# Visualization of Features
st.markdown('## Features')

fig, ax = plt.subplots(1, 2, figsize=(15, 7))

try:
    amount_val = df['Amount'].values
    time_val = df['Time'].values
except KeyError:
    amount_val = df['scaled_amount'].values
    time_val = df['scaled_time'].values

sns.distplot(amount_val, ax=ax[0], color='r')
ax[0].set_title('Distribution of Transaction Amount', fontsize=14)
ax[0].set_xlim([min(amount_val), max(amount_val)])

sns.distplot(time_val, ax=ax[1], color='b')
ax[1].set_title('Distribution of Transaction Time', fontsize=14)
ax[1].set_xlim([min(time_val), max(time_val)])

st.pyplot(fig)
