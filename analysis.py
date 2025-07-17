import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# Folder where your downloaded .tif files are saved
data_folder = "data_file"

# Initialize
lahore_means = []
potsdam_means = []
years = list(range(2013, 2022))

for year in years:
    # File paths
    lahore_file = os.path.join(data_folder, f"Lahore_VIIRS_{year}.tif")
    potsdam_file = os.path.join(data_folder, f"Potsdam_VIIRS_{year}.tif")
    
    # Read Lahore
    with rasterio.open(lahore_file) as src:
        lahore_data = src.read(1)
        lahore_mean = np.mean(lahore_data[lahore_data > 0])  # exclude zero or no-data
        lahore_means.append(lahore_mean)
    
    # Read Potsdam
    with rasterio.open(potsdam_file) as src:
        potsdam_data = src.read(1)
        potsdam_mean = np.mean(potsdam_data[potsdam_data > 0])
        potsdam_means.append(potsdam_mean)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(years, lahore_means, label="Lahore", marker='o')
plt.plot(years, potsdam_means, label="Potsdam", marker='o')
plt.title("Average Nightlight Brightness (VIIRS)")
plt.xlabel("Year")
plt.ylabel("Mean Radiance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
