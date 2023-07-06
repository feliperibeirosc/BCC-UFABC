import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/r7ze25zg7w5eriv/temperaturas_estat1.csv?dl=1")

df["razão"] = df["temperatura"] / df["periodo"]

print(df)