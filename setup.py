import numpy as npy
import csv
import plotly.express as plt

def plot_figure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = plt.scatter(df, x="Temperature", y = "Ice-cream Sales")
        fig.show()

def get_data_source(data_path):
    temp_sales = []
    icecream_sales = []
    with open(data_path) as f:
        r = csv.DictReader(f)
        print(r[1])

        for i in r:
            temp_sales.append(float(r["Temperature"]))
            icecream_sales.append(float(r["Ice-cream Sales"]))

    return {
        "x": temp_sales,
        "y": icecream_sales
    }

def find_correlation(data_source):
    correlation = npy.corrcoef(data_source["x"], data_source["y"])
    print("Correlation is",  correlation[0, 1])

def setup():
    data_path = "d1.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()
