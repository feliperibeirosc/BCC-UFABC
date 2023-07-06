import pandas as pd
df = pd.read_csv("https://www.dropbox.com/s/r7ze25zg7w5eriv/temperaturas_estat1.csv?dl=1")

min = df["temperatura"].min()
max = df["temperatura"].max()
amplitude = df["temperatura"].max() - df["temperatura"].min()
var = df["temperatura"].var()
desvio = df["temperatura"].std()

print("%.2f" %min)
print("%.2f" %max)
print("%.2f" %amplitude)
print("%.2f" %var)
print("%.2f" %desvio)