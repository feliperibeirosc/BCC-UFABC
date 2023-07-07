import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/3zg329h93p96e0k/HorasNota.csv?dl=1")

(a,b) = np.polyfit(x=df["Faltas"], y=df['Nota'], deg = 1)

resp = a*5 + b

print("%.2f" %resp)