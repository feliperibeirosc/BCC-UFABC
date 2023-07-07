import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/3zg329h93p96e0k/HorasNota.csv?dl=1")

r = (df['Nota'].corr(df['Faltas']))**2


print("%.2f" %r)