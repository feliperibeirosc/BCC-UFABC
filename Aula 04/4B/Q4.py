import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/08mj9xfm8f6p9ph/fake-classrooms05.csv?dl=1")

media = df["Prova 2"].mean()

print("%.2f" %media)