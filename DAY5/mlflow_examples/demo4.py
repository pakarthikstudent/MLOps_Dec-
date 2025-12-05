import mlflow

mlflow.set_experiment("my_data")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.23)
    
    # Log a dictionary directly as an artifact
    mlflow.log_dict({"status": "completed", "notes": "example run"}, "info.json")

print("Run completed! Start MLflow UI with: mlflow ui")