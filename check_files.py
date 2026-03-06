import os

olr_folder = "olr_data"
rain_folder = "rainfall_data"

print("Number of OLR files:", len(os.listdir(olr_folder)))
print("Number of Rainfall files:", len(os.listdir(rain_folder)))