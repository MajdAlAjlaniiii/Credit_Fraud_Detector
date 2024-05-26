from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

def train_models(X_train, y_train):
    classifiers = {
        "LogisiticRegression": LogisticRegression(),
        "KNearest": KNeighborsClassifier(),
        "Support Vector Classifier": SVC(),
        "DecisionTreeClassifier": DecisionTreeClassifier()
    }
    
    trained_models = {}
    for name, model in classifiers.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
    
    return trained_models

def tune_models(X_train, y_train, models):
    params = {
        "LogisiticRegression": {"penalty": ['l1', 'l2'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
        "KNearest": {"n_neighbors": list(range(2,5,1)), 'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']},
        "Support Vector Classifier": {'C': [0.5, 0.7, 0.9, 1], 'kernel': ['rbf', 'poly', 'sigmoid', 'linear']},
        "DecisionTreeClassifier": {"criterion": ["gini", "entropy"], "max_depth": list(range(2,4,1)), "min_samples_leaf": list(range(5,7,1))}
    }
    
    tuned_models = {}
    for name, model in models.items():
        grid = GridSearchCV(model, params[name])
        grid.fit(X_train, y_train)
        tuned_models[name] = grid.best_estimator_
    
    return tuned_models
