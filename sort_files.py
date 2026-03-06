import os
import h5py
import shutil

source_folder = "data"
olr_folder = "olr_data"
rain_folder = "rainfall_data"

os.makedirs(olr_folder, exist_ok=True)
os.makedirs(rain_folder, exist_ok=True)

for file in os.listdir(source_folder):

    if file.endswith(".h5"):
        file_path = os.path.join(source_folder, file)

        try:
            f = h5py.File(file_path, 'r')
            keys = list(f.keys())

            # Detect OLR files
            if "OLR_DLY" in keys:
                shutil.move(file_path, os.path.join(olr_folder, file))
                print("Moved to OLR:", file)

            # Detect Rainfall files
            elif "IMR_DLY" in keys or "rain" in str(keys).lower():
                shutil.move(file_path, os.path.join(rain_folder, file))
                print("Moved to Rainfall:", file)

            else:
                print("Unknown file:", file)

        except:
            print("Error reading:", file)

print("Sorting completed")