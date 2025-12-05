#  Descriptive names based on hyperparameters
import mlflow

mlflow.set_experiment("my_samples")

learning_rate = 0.01
batch_size = 32
model_type = "RandomForest"

run_name = f"{model_type}_lr{learning_rate}_batch{batch_size}"

with mlflow.start_run(run_name=run_name):
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("batch_size", batch_size)
    mlflow.log_param("model_type", model_type)
    mlflow.log_metric("accuracy", 0.95)