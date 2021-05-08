import csv
import plotly.express as plt

with open("d4.csv") as f:
    df = csv.DictReader(f)
    fig = plt.scatter(df,x = "Coffee in ml", y = "sleep in hours")
    fig.show()