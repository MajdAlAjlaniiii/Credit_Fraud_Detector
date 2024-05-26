"""Project pipelines."""
from typing import Dict

from typing import Dict
from kedro.pipeline import Pipeline

from credit_fraud_detector.pipelines import data_preprocessing
from credit_fraud_detector.pipelines import data_split
from credit_fraud_detector.pipelines import dimensionality_reduction
from credit_fraud_detector.pipelines import model_training
from credit_fraud_detector.pipelines import model_evaluation


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_preprocessing_pipeline = data_preprocessing.create_pipeline()
    data_split_pipeline = data_split.create_pipeline()
    dimensionality_reduction_pipeline = dimensionality_reduction.create_pipeline()
    model_training_pipeline = model_training.create_pipeline()
    model_evaluation_pipeline = model_evaluation.create_pipeline()
    return {
        "data_preprocessing": data_preprocessing_pipeline,
        "data_split": data_split_pipeline,
        "dimensionality_reduction": dimensionality_reduction_pipeline,
        "model_training": model_training_pipeline,
        "model_evaluation": model_evaluation_pipeline,
        "__default__": data_preprocessing_pipeline + data_split_pipeline + dimensionality_reduction_pipeline + model_training_pipeline + model_evaluation_pipeline
    }
