import pandas as pd

# Load clean datasets
olr = pd.read_csv("olr_dataset_clean.csv")
rain = pd.read_csv("rainfall_dataset_clean.csv")

print("OLR shape:", olr.shape)
print("Rainfall shape:", rain.shape)

# Merge on Latitude and Longitude
merged = pd.merge(olr, rain, on=["Latitude", "Longitude"])
print("Merged dataset shape:", merged.shape)

# Save final dataset
merged.to_csv("final_dataset_clean.csv", index=False)
print("Final merged dataset saved!")