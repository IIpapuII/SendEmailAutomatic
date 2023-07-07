import pandas as pd

df = pd.read_excel('SendEmailAutomatic/scripts/docs/ClientesDeudores.xlsx', header=None)
df_array = df.values

for j in range(len(df_array)):
    print(df_array[j])
