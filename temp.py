import csv
import plotly.express as plt

with open("d1.csv") as f:
    df = csv.DictReader(f)
    fig = plt.scatter(df,x = "Temperature", y = "Ice-cream Sales")
    fig.show()