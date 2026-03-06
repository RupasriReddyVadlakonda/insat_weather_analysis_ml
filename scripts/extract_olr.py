import h5py
import os
import pandas as pd
import numpy as np

olr_folder = "olr_data"
data = []

for file in os.listdir(olr_folder):

    if not file.endswith(".h5"):
        continue

    path = os.path.join(olr_folder, file)
    print("Processing:", file)

    with h5py.File(path, 'r') as f:

        lat = f['Latitude'][:]        # already 2D
        lon = f['Longitude'][:]       # already 2D
        olr = f['OLR_DLY'][:][0]      # remove time dimension

        # Flatten arrays directly
        lat_flat = lat.flatten()
        lon_flat = lon.flatten()
        olr_flat = olr.flatten()

        # Remove invalid values
        mask = olr_flat != -999
        lat_flat = lat_flat[mask]
        lon_flat = lon_flat[mask]
        olr_flat = olr_flat[mask]

        # Reduce dataset size (sampling)
        sample_step = 20
        lat_flat = lat_flat[::sample_step]
        lon_flat = lon_flat[::sample_step]
        olr_flat = olr_flat[::sample_step]

        # Stack arrays efficiently
        stacked = np.column_stack((lat_flat, lon_flat, olr_flat))
        data.append(stacked)

# Combine all files
data = np.vstack(data)

df = pd.DataFrame(data, columns=["Latitude", "Longitude", "OLR"])
df.to_csv("olr_dataset_clean.csv", index=False)

print("Clean OLR dataset saved:", df.shape)