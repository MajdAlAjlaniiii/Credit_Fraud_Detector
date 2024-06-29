import shap
import pandas as pd
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

def calculate_and_plot_shap(model, data: pd.DataFrame):
    output_path = "data/08_reporting/shap_summary_plot.png"
    logger.info("Calculating SHAP values...")
    explainer = shap.Explainer(model, data)
    shap_values = explainer(data)
    
    logger.info("Generating SHAP summary plot...")
    plt.figure()
    shap.summary_plot(shap_values, data, show=False)
    plt.savefig(output_path)
    logger.info(f"SHAP summary plot saved to {output_path}")