from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import yaml

def train_models(X_train, y_train):
    classifiers = {
        "LogisiticRegression": LogisticRegression(),
        "KNearest": KNeighborsClassifier(),
        "Support Vector Classifier": SVC(),
        "DecisionTreeClassifier": DecisionTreeClassifier()
    }

    trained_models = {}
    for name, model in classifiers.items():
        with mlflow.start_run(run_name=f"training_{name}", nested=True):
            model.fit(X_train, y_train)
            trained_models[name] = model
            
            # Log model parameters
            mlflow.log_params(model.get_params())
            
            # Save the model as an artifact
            mlflow.sklearn.log_model(model, artifact_path=name)
            
            # Set a tag for this run
            mlflow.set_tag("model_type", name)
            
    return trained_models

def tune_models(X_train, y_train, models):
    params = {
        "LogisiticRegression": {"penalty": ['l1', 'l2'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
        "KNearest": {"n_neighbors": list(range(2,5,1)), 'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']},
        "Support Vector Classifier": {'C': [0.5, 0.7, 0.9, 1], 'kernel': ['rbf', 'poly', 'sigmoid', 'linear']},
        "DecisionTreeClassifier": {"criterion": ["gini", "entropy"], "max_depth": list(range(2,4,1)), "min_samples_leaf": list(range(5,7,1))}
    }

    tuned_models = {}

    with open('conf/local/mlflow.yml') as f:
        experiment_name = yaml.load(f, Loader=yaml.loader.SafeLoader)['tracking']['experiment']['name']
    experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

    for name, model in models.items():
        with mlflow.start_run(experiment_id=experiment_id, run_name=f"tuning_{name}", nested=True):
            mlflow.sklearn.autolog()  # Enable autologging for sklearn models

            grid = GridSearchCV(model, params[name])
            grid.fit(X_train, y_train)

            best_model = grid.best_estimator_
            tuned_models[name] = best_model

            # Log best parameters and performance metrics
            mlflow.log_params(grid.best_params_)
            mlflow.log_metric("best_score", grid.best_score_)

            # Log the tuned model as an artifact
            mlflow.sklearn.log_model(best_model, artifact_path=f"tuned_{name}")

            # Log custom tags or additional information
            mlflow.set_tag("model_type", name)
            mlflow.set_tag("tuning", "GridSearchCV")

            # Optionally, log specific metrics on training data (example: training accuracy)
            y_train_pred = best_model.predict(X_train)
            train_accuracy = accuracy_score(y_train, y_train_pred)
            mlflow.log_metric("train_accuracy", train_accuracy)

    return tuned_models
