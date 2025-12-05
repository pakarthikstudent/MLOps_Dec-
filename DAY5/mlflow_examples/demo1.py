import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("my_demo")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    
    # Log metrics
    mlflow.log_metric("accuracy", 0.95)

    mlflow.log_metric("loss", 0.23)
