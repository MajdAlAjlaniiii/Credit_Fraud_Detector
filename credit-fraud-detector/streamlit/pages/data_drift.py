import os
import json

import pandas as pd
import streamlit as st

from modules.nav import NavigationBar
from modules.pipes import DisplayPipeExecution
from modules.data import get_data, plot_feats




# Page configuration
st.set_page_config(
    page_title="Data Drift",
    page_icon="./images/pastel-de-nata.png",
    layout='wide')

NavigationBar()



# Page content
st.markdown('# Here you can simulate data drift and check the resulting dataset')

original_df = get_data('Preprocessed')
st.dataframe(original_df)
