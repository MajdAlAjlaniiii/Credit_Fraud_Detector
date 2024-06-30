# Credit Fraud Detector

## Overview
The **Credit Fraud Detector** is a project developed as part of our Machine Learning Operations (MLOps) course. This project aims to simulate a real-world process of developing, deploying, and maintaining a machine learning model to detect fraudulent credit card transactions.


## Team Members
**Group G**
- **Diogo Pires** (ID: 20230534)
- **Majd Al Ajlani** (ID: 20230767)
- **Manuel Gonçalves** (ID: 20230466)
- **Maria Batrakova** (ID: 20230739)
- **Vitor Souto Neves** (ID: 20230548)

## **Project Structure**
The project is structured using the Kedro framework, which ensures modularity, reproducibility, and maintainability of the data science workflow. With the main components as follows:

```
├── conf                              # Configuration files used by Kedro
├── data                              # Data storage
│   ├── 01_raw
│   ├── 02_intermediate
│   ├── 03_primary
│   ├── 05_model_input
│   ├── 06_models
│   └── 08_reporting
├── notebooks                         # Jupyter notebooks used
├── docs/source
├── src                               # Source code for use in this project
│   ├── credit_fraud_detector
│   │   └── pipelines
│   └── pipelines/data_unit_tests/gx
│   ├── streamlit
├── tests                             # Tests for the project
└── requirements.txt
```

## **Main MLOps Tools used**

- **Kedro**: For organizing pipelines and modularizing code.
- **Hopsworks**: For creating and managing a feature store.
- **MLFlow**: For tracking pipeline executions, hyperparameter tuning experiments, and model comparisons.
- **SHAP Values**: For model explainability.
- **Data Drift Tests**: For monitoring changes in data distribution over time.
- **Data Unit Tests**: For ensuring data integrity and correctness.
- **Streamlit**: For developing interactive, user-friendly applications to visualize model results and performance metrics.
