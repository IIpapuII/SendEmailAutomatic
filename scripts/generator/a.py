import pandas as pd
import os

df = pd.read_excel(os.path.join(os.path.dirname(os.path.abspath('scripts')),'SendEmailAutomatic/scripts/docs/ClientesDeudores.xlsx'), header=None)
df_array = df.values

for j in range(len(df_array)):
    print(df_array[j], "        ", j)
