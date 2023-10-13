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
print(df_mestrado.head(10), end="\n")

# Medidas de tendência central e dispersão
mestrado_conceito_medio_media = df_mestrado["Conceito Médio de Mestrado"].mean()
print("Média de Conceito Médio de Mestrado: ", mestrado_conceito_medio_media, end="\n")

mestrado_conceito_medio_mediana = df_mestrado["Conceito Médio de Mestrado"].median()
print("Mediana de Conceito Médio de Mestrado: ", mestrado_conceito_medio_mediana, end="\n")

mestrado_conceito_medio_std = df_mestrado["Conceito Médio de Mestrado"].std()
print("Desvio Padrão de Conceito Médio de Mestrada: ", mestrado_conceito_medio_std, end="\n")

mestrado_conceito_medio_max = df_mestrado["Conceito Médio de Mestrado"].max()
print("Conceito Médio de Mestrado Máximo: ", mestrado_conceito_medio_max, end="\n") 

mestrado_conceito_medio_min = df_mestrado["Conceito Médio de Mestrado"].min()
print("Conceito Médio de Mestrado Mínimo: ", mestrado_conceito_medio_min, end="\n")