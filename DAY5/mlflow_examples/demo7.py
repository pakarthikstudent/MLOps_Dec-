import mlflow

mlflow.set_experiment("hyperparameter_tuning")

learning_rates = [0.001, 0.01, 0.1]

for i, lr in enumerate(learning_rates):
    run_name = f"run_{i+1}_lr_{lr}"
    
    with mlflow.start_run(run_name=run_name):
        mlflow.log_param("learning_rate", lr)
        # Simulate training
        accuracy = 0.8 + (lr * 10)  # dummy calculation
        mlflow.log_metric("accuracy", accuracy)