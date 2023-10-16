import pandas as pd

# Lendo o arquivo XLSX
df_xlsx = pd.read_excel("IGC_2021.xlsx")

# Convertendo o arquivo para CSV
df_xlsx.to_csv("IGC_2021.csv", index=False)

df = pd.read_csv("IGC_2021.csv")
# As linhas de indice 2012 e 2013 não contém dados, logo são removidas
df.drop(index=[2012, 2013], inplace = True)
