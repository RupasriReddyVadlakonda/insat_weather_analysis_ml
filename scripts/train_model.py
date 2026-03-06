import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

print("Loading dataset...")
df = pd.read_csv("final_dataset.csv")
print("Original dataset shape:", df.shape)
# Reduce dataset size for faster training
df = df.sample(200000, random_state=42)
print("Sampled dataset shape:", df.shape)
# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
# Drop missing values
df = df.dropna()
# Features and target
X = df[["Latitude", "Longitude", "OLR"]]
y = df["Rainfall"]
print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)
# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
print("\nTraining Random Forest Model...")
model = RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    n_jobs=-1,
    random_state=42
)
model.fit(X_train, y_train)
print("Model training completed.")
# Predictions
pred = model.predict(X_test)
# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, pred))
print("\nModel Evaluation")
print("RMSE:", rmse)
# Save model
joblib.dump(model, "rainfall_prediction_model.pkl")
print("\nModel saved as rainfall_prediction_model.pkl")