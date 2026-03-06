import h5py
import os

# Folder containing HDF5 files
folder = "rainfall_data"   # change to olr_data if needed

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    print("\n==============================")
    print("File:", file)
    print("==============================")
    with h5py.File(path, 'r') as f:

        for key in f.keys():

            dataset = f[key]

            print("\nDataset:", key)
            print("Shape:", dataset.shape)
            print("Dtype:", dataset.dtype)