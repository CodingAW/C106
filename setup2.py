import numpy as npy
import csv
import plotly.express as plt

def get_data_source(data_path):
    temp_sales = []
    icecream_sales = []
    with open(data_path) as f:
        df = csv.DictReader(f)

        for i in df:
            temp_sales.append(float(df["Coffee in ml"]))
            icecream_sales.append(float(df["sleep in hours"]))

    return {
        "x": temp_sales,
        "y": icecream_sales
    }

def find_correlation(data_source):
    correlation = npy.corrcoef(data_source["x"], data_source["y"])
    print(f"Correlation is {correlation[0, 1]}")

def setup():
    data_path = "d4.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()