import mlflow

mlflow.set_experiment("my_samples")

with mlflow.start_run(run_name="my_sample1_runName"):
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.23)