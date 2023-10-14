import func_analises as fan
import limpa_dados as lp
import matplotlib.pyplot as plt
import pandas as pd

df = lp.corrige_nomes_df(lp.df)

# Análise "Instituições de Ensino por UF"
sigla_uf = df["Sigla da UF"]
print(sigla_uf, end="\n")

ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
print(ocorrencia_por_uf, end="\n")

# Análise "Conceito Médio de Mestrado"
df_mestrado = fan.selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
print(df_mestrado, end="\n")

# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_mestrado, "Conceito Médio de Mestrado"))