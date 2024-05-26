from sklearn.metrics import classification_report

def evaluate_models(X_test, y_test, models):
    evaluation_reports = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        evaluation_reports[name] = report
    return evaluation_reports
