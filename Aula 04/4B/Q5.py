import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/pk3nk4mafrerijl/fake-classrooms10.csv?dl=1")

var = df["Prova 2"].var()

print("%.2f" %var)