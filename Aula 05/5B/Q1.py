import pandas as pd
import numpy as np
df = pd.read_csv("https://www.dropbox.com/s/ahlznbnx07dfpqt/Exames3.csv?dl=1")
coluna = input('Digite a coluna da planilha (Exame 2 ou Exame 3)')

r = df[coluna].corr(df['Exame 1'])
print("%.2f" %r)