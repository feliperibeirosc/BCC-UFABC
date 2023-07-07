import pandas as pd
import numpy as np

df = pd.read_csv("https://www.dropbox.com/s/del14yip68hwyy0/CafeNota.csv?dl=1")

(a, b, c, d) =  np.polyfit(x=df['Cafes'], y=df['Nota'], deg= 3)

print("%.2f" % a)
print("%.2f" % b)
print("%.2f" % c)
print("%.2f" % d)
