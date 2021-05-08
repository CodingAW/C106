import csv
import plotly.express as plt

with open("d2.csv") as f:
    df = csv.DictReader(f)
    fig = plt.scatter(df,x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
    fig.show()