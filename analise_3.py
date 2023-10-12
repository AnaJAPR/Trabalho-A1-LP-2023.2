import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

df = lp.df

# Análise "Instituições de Ensino por UF"
sigla_uf = df["Sigla da UF"]
print(sigla_uf, end="\n")

ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
print(ocorrencia_por_uf, end="\n")

# Análise "Beta"
df_analise_beta = df[["Sigla da UF", "Beta (Proporção de Mestrado - Equivalente)"]]
print(df_analise_beta)