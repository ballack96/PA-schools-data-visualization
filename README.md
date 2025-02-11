# PA Schools Data Visualization Dashboard

This repository contains a Python-based Plotly dashboard visualizing data on Pennsylvania schools.  It includes the data processing notebook used to generate the data, the dashboard code, and the resulting data file.

## Overview

This project provides an interactive dashboard built using Plotly in Python. The dashboard visualizes key data points related to Pennsylvania schools, offering insights into [mention specific insights or visualizations offered by your dashboard, e.g., student performance, demographics, funding, etc.].  The data used in this dashboard is processed from a CSV file using a Jupyter Notebook.

## Installation

To run this dashboard locally, you'll need to have Python and several libraries installed.  Follow these steps:

1. **Clone the Repository:**

  ```bash
  git clone https://github.com/ballack96/PA-schools-data-visualization.git

  cd PA-schools-data-visualization
  ```
2. **Create a Virtual Environment**

  > It's best practice to use a virtual environment to manage dependencies. 
  
  ```bash
  python3 -m venv .venv  # Create a virtual environment

  source .venv/bin/activate  # Activate the environment (Linux/macOS)

  .venv\Scripts\activate  # Activate the environment (Windows)
  ```

3. Install Dependencies:
   
  ```bash
  pip install -r requirements.txt
  ```

  > If you don't have a ***requirements.txt*** file yet, create one:

  ```bash
  pip freeze > requirements.txt
  ```

## Data Processing

The data_processing.ipynb notebook processes the raw data from the CSV file ([name of CSV file].csv) and generates the data file used by the dashboard ([name of output data file].csv or whatever format you use).

## Running the Dashboard

The dashboard is run using a Python script(activate your virtual environment if you created one)

1. Run the Script

  ```bash
  python app.py 

  ```
2. Access the Dashboard: The script will typically provide a URL (usually http://127.0.0.1:8050/ or similar) that you can open in your web browser to view the dashboard.

## File Structure

```
  PA-schools-data-visualization/
  ├── data_processing.ipynb     # Jupyter Notebook for data processing
  ├── [name of CSV file].csv    # Raw data source
  ├── [name of output data file].csv # Processed data used by the dashboard
  ├── app.py             # Python script for running the Plotly dashboard
  ├── requirements.txt         # List of required Python packages
  └── README.md                # This file
```
