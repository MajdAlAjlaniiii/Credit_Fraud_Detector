"""Project pipelines."""
from typing import Dict

from typing import Dict
from kedro.pipeline import Pipeline

from credit_fraud_detector.pipelines import data_preprocessing
from credit_fraud_detector.pipelines import data_split

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_preprocessing_pipeline = data_preprocessing.create_pipeline()
    data_split_pipeline = data_split.create_pipeline()

    return {
        "data_preprocessing": data_preprocessing_pipeline,
        "data_split": data_split_pipeline
    }
