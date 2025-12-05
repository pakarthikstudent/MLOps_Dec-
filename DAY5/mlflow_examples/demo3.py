import mlflow

mlflow.set_experiment("my_demo")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.23)
    
    # Create and log a simple text file
    with open("results.txt", "w") as f:
        f.write("Training completed successfully\n")
        f.write("Final accuracy: 0.95\n")
    
    mlflow.log_artifact("results.txt")

print("Run completed! Start MLflow UI with: mlflow ui")