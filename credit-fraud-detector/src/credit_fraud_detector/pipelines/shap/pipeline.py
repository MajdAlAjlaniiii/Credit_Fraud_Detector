from kedro.pipeline import Pipeline, node, pipeline
from .nodes import calculate_and_plot_shap

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=calculate_and_plot_shap,
                inputs=["trained_models", "preprocessed_data"],
                outputs=None,
                name="calculate_and_plot_shap",
            ),
        ]
    )
