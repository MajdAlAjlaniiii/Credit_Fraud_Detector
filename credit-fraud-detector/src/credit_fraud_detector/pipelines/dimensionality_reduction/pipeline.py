from kedro.pipeline import Pipeline, node
from .nodes import apply_dimensionality_reduction

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=apply_dimensionality_reduction,
                inputs="preprocessed_data",
                outputs="reduced_data",
                name="apply_dimensionality_reduction_node"
            ),
        ]
    )
