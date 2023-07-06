import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/r7ze25zg7w5eriv/temperaturas_estat1.csv?dl=1")
p25 = np.percentile(df["temperatura"], q=25)
p50 = np.percentile(df["temperatura"], q=50)
p75 = np.percentile(df["temperatura"], q=75)
print("%.2f" %p25)
print("%.2f" %p50)
print("%.2f" %p75)