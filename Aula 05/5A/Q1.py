import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/3zg329h93p96e0k/HorasNota.csv?dl=1")

r = df['Chocolate'].corr(df['Faltas'])
print("%.2f" %r)