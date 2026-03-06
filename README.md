# Satellite Rainfall Analysis using INSAT-3DR Data

## Overview

This project analyzes satellite-derived rainfall data using data from **INSAT-3DR**. The workflow involves extracting geospatial rainfall and radiation data from HDF5 satellite files, converting them into usable datasets, visualizing rainfall distribution, and applying a machine learning model to analyze rainfall patterns.

The project demonstrates a full pipeline commonly used in remote sensing and meteorological data analysis.

## Data Source

Satellite data used in this project comes from:

* INSAT-3DR satellite
* MOSDAC (Meteorological and Oceanographic Satellite Data Archival Centre)

Datasets used:

* OLR (Outgoing Longwave Radiation)
* IMR (INSAT Multispectral Rainfall)

Note: Due to large file sizes, datasets are not included in this repository.

## Project Workflow

Satellite HDF5 Data
↓
Data Extraction using Python (h5py)
↓
Dataset Creation (Latitude, Longitude, Rainfall, OLR)
↓
Data Cleaning and Sampling
↓
Rainfall Visualization (Geospatial Mapping)
↓
Machine Learning Model
↓
Model Evaluation (RMSE)

## Repository Structure

insat_project
│
├── scripts
│   ├── extract_olr.py
│   ├── extract_rainfall.py
│
├── visualization.py
├── model.py
├── README.md
└── .gitignore

Dataset folders (ignored by Git):

* olr_data/
* rainfall_data/
* data/

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* h5py
* Scikit-learn

## Visualization

The rainfall distribution is visualized using latitude-longitude satellite grids to understand spatial rainfall patterns detected by INSAT-3DR.

## Machine Learning

A machine learning regression model was trained to analyze rainfall patterns.

Evaluation metric:

RMSE = 0.00057

This value reflects the prediction error between actual rainfall values and predicted rainfall values.

## How to Run the Project

1. Clone the repository

git clone https://github.com/yourusername/insat_project.git

2. Install dependencies

pip install numpy pandas matplotlib h5py scikit-learn

3. Run data extraction scripts

python scripts/extract_olr.py
python scripts/extract_rainfall.py

4. Run visualization

python visualization.py

5. Run machine learning model

python model.py

## Applications

* Satellite rainfall monitoring
* Meteorological data analysis
* Remote sensing research
* Climate data analysis
* Machine learning for geospatial data

## Future Improvements

* Add time-series rainfall analysis
* Improve rainfall prediction models
* Integrate additional satellite parameters
* Build interactive geospatial visualizations

