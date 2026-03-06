import pandas as pd
import joblib
model = joblib.load("c")
test_points = pd.DataFrame({
    "Latitude": [15.3, 16.1, 17.5, 18.0],
    "Longitude": [78.2, 79.0, 80.3, 81.5],
    "OLR": [240, 245, 250, 260]  # vary OLR values
})
predictions = model.predict(test_points)
print("Predicted Rainfall: ", predictions)