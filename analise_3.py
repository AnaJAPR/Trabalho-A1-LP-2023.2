import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

df = lp.corrige_nomes_df(lp.df)

# Análise "Instituições de Ensino por UF"
sigla_uf = df["Sigla da UF"]
print(sigla_uf, end="\n")

ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
print(ocorrencia_por_uf, end="\n")

# Análise "Conceito Médio de Mestrado"
df_mestrado = df[["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"]].astype(float)
df_mestrado = df_mestrado[(df_mestrado["Beta (Proporção de Mestrado - Equivalente)"] != 0) & (df_mestrado["Beta (Proporção de Mestrado - Equivalente)"].notna())]
print(df_mestrado.head(10))

# Medidas de tendência central e dispersão
mestrado_conceito_medio_media = df_mestrado["Conceito Médio de Mestrado"].mean()
print(mestrado_conceito_medio_media)

mestrado_conceito_medio_mediana = df_mestrado["Conceito Médio de Mestrado"].median()
print(mestrado_conceito_medio_mediana)

mestrado_conceito_medio_std = df_mestrado["Conceito Médio de Mestrado"].std()
print(mestrado_conceito_medio_std)

mestrado_conceito_medio_max = df_mestrado["Conceito Médio de Mestrado"].max()
print(mestrado_conceito_medio_max) 

mestrado_conceito_medio_min = df_mestrado["Conceito Médio de Mestrado"].min()
print(mestrado_conceito_medio_min)