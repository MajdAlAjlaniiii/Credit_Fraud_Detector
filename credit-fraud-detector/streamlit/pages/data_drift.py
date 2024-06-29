import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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

run_button = st.button('Run the drift pipeline')
reporter = st.empty()

if not run_button:
    reporter.markdown('## Before the drift')
    plot_feats(original_df)
else:
    DisplayPipeExecution('drift', delete_after_execution=True)

    drift_df = get_data('Drift')
    drift_analysis_df = get_data('Drift Analysis')
    reporter.markdown('## After the drift')

    st.markdown('### Features after simulated drift')
    plot_feats(drift_df)

    st.markdown('### Analysis results')
    st.dataframe(drift_analysis_df)

    # Get bad column example and plot side by side
    bad_column = drift_analysis_df[drift_analysis_df.Success != 1].Column.values[0]

    before = original_df[bad_column].values
    after = drift_df[bad_column].values
    fig, axs = plt.subplots(1, 2, figsize=(15,7))
    sns.distplot(before, ax=axs[0], color='r')
    sns.distplot(after, ax=axs[1], color='b')
    axs[0].set_title(f'{bad_column.capitalize()} before drift', fontsize=14)
    axs[1].set_title(f'{bad_column.capitalize()} after drift', fontsize=14)

    st.pyplot(fig)
