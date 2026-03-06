import os
import h5py
import pandas as pd
import numpy as np
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rainfall_folder = os.path.join(base_dir, "rainfall_data")
dataframes = []
for file in os.listdir(rainfall_folder):
    if file.endswith(".h5"):
        filepath = os.path.join(rainfall_folder, file)
        print("Processing:", file)
        with h5py.File(filepath, 'r') as f:
            rainfall = f['IMR_DLY'][:]      # (time, lat, lon)
            lat = f['latitude'][:]
            lon = f['longitude'][:]
            rainfall = rainfall[0]          # remove time dimension
            lon_grid, lat_grid = np.meshgrid(lon, lat)
            df = pd.DataFrame({
                "latitude": lat_grid.flatten(),
                "longitude": lon_grid.flatten(),
                "rainfall": rainfall.flatten()
            })
            dataframes.append(df)
final_df = pd.concat(dataframes)
final_df.to_csv(os.path.join(base_dir, "rainfall_extracted.csv"), index=False)
print("Extraction Completed")