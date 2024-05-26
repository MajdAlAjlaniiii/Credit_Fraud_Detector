
"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node
from .nodes import split_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=split_data,
            inputs="preprocessed_data",
            outputs=["original_Xtrain", "original_Xtest", "original_ytrain", "original_ytest"],
            name="split_data_node",
        ),
    ])
