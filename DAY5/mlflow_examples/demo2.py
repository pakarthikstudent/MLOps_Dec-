import mlflow
import pickle

mlflow.set_experiment("my_demo")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.23)
    
    # Create a sample file to log
    sample_data = {"model": "example"}
    with open("model.pkl", "wb") as f:
        pickle.dump(sample_data, f)
    
    # Now log the artifact
    mlflow.log_artifact("model.pkl")

print("Run completed! Start MLflow UI with: mlflow ui")