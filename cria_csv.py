import pandas as pd

# Lendo o arquivo XLSX
df_xlsx = pd.read_excel("IGC_2021.xlsx")

# Convertendo o arquivo para CSV
df_xlsx.to_csv("IGC_2021.csv", index=False)
