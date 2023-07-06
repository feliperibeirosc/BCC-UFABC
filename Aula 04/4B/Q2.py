import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/0g4i2s506tji6ya/fake-classrooms06.csv?dl=1")
p58 = np.percentile(df["Trabalho"], q=58)
print("%.2f" %p58)