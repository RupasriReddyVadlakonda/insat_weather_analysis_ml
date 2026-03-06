import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("rainfall_dataset.csv")

# keep only rainfall > 0
df = df[df["Rainfall"] > 0]

plt.figure(figsize=(8,6))

plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["Rainfall"],
    s=5
)

plt.colorbar(label="Rainfall (mm)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Rainfall Events from INSAT-3DR")

plt.show()
