import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn

# Load dataset
data = pd.read_csv("../inputs/data.txt")

# Features and target
X = data[["Temperature"]]
y = data["IceCreamSales"]

# Train model
model = LinearRegression()

with mlflow.start_run():

    model.fit(X, y)

    prediction = model.predict([[29]])

    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("prediction_for_29C", prediction[0])

    mlflow.sklearn.log_model(model, "model")

print("Prediction for 29°C:", prediction[0])
