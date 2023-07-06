import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/2j4qfp81btv0k4t/fake-classrooms07.csv?dl=1")

df["Ponderada"] = df["Prova 2"] * 3 + df["Trabalho"] * 7

print(df)