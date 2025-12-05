import mlflow
from datetime import datetime

# Set experiment
mlflow.set_experiment("sample_run_name_demo")

# Define hyperparameters
configs = [
    {"lr": 0.001, "epochs": 10, "model": "LogisticRegression"},
    {"lr": 0.01, "epochs": 20, "model": "RandomForest"},
    {"lr": 0.1, "epochs": 15, "model": "XGBoost"}
]

for config in configs:
    # Create descriptive run name
    run_name = f"{config['model']}_lr{config['lr']}_epochs{config['epochs']}"
    
    with mlflow.start_run(run_name=run_name):
        # Log parameters
        mlflow.log_param("learning_rate", config['lr'])
        mlflow.log_param("epochs", config['epochs'])
        mlflow.log_param("model_type", config['model'])
        
        # Add tags
        mlflow.set_tag("timestamp", datetime.now().isoformat())
        mlflow.set_tag("status", "completed")
        
        # Simulate metrics
        accuracy = 0.85 + (config['lr'] * 5)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("loss", 1 - accuracy)

print("Runs completed! View them with: mlflow ui")