from kedro.pipeline import Pipeline, node
from .nodes import train_models, tune_models

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=train_models,
                inputs=["X_train_data", "y_train_data"],
                outputs="trained_models",
                name="train_models_node",
            ),
            node(
                func=tune_models,
                inputs=["X_train_data", "y_train_data", "trained_models"],
                outputs="tuned_models",
                name="tune_models_node",
            ),
        ],
        tags='train'
    )
