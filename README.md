#  VIIRS Nightlight Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Comparative analysis of VIIRS nighttime light data between Lahore (Pakistan) and Potsdam (Germany) from 2013-2021.

![Sample Output](Compare of Potsdam_Lahore)

##  Features
- Processes VIIRS .tif files to extract mean radiance values
- Comparative trend visualization
- Handles missing/no-data values gracefully
- Outputs publication-ready figures and CSV results

##  Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/viirs-nightlight-analysis.git
   cd viirs-nightlight-analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your VIIRS data**:
   - Place `.tif` files in `data/` following `{City}_VIIRS_{Year}.tif` format

4. **Run analysis**:
   ```bash
   python scripts/analysis.py
   ```

##  Data Requirements
VIIRS nighttime light data in GeoTIFF format (annual composites recommended).  
Example sources:
- [NASA Black Marble](https://blackmarble.gsfc.nasa.gov/)
- [Earth Observation Group](https://eogdata.mines.edu/products/vnl/)

##  Outputs
- `outputs/figures/trends.png`: Comparative plot
- `outputs/results/trends.csv`: Processed data

##  Contributing
Pull requests welcome! For major changes, please open an issue first.

##  License
[MIT](LICENSE)
