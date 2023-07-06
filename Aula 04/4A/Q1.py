import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/r7ze25zg7w5eriv/temperaturas_estat1.csv?dl=1")

media = df["temperatura"].mean()
mediana =df["temperatura"].median()

print("%.2f" %media)
print("%.2f" %mediana)