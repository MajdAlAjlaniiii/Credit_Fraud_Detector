"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from credit_fraud_detector.pipelines import data_preprocessing

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    data_preprocessing_pipeline = data_preprocessing.create_pipeline()
    # pipelines["__default__"] = sum(pipelines.values())
    return {"__default__": data_preprocessing_pipeline}

