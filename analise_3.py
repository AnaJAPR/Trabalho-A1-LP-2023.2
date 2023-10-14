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

# Análise "Conceito Médio"
# "Graduação"
df_graduacao = fan.selecionar_colunas_eliminando_nulos(df, ["Alfa (Proporção de Graduação)", "Conceito Médio de Graduação"])
print(df_graduacao)
# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_graduacao, "Conceito Médio de Graduação"))

# "Mestrado"
df_mestrado = fan.selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
print(df_mestrado, end="\n")
# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_mestrado, "Conceito Médio de Mestrado"))

# "Doutorado"
df_doutorado = fan.selecionar_colunas_eliminando_nulos(df, ["Gama (Proporção de Doutorandos – Equivalente)", "Conceito Médio do doutorado"])
print(df_doutorado)
# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_doutorado, "Conceito Médio do doutorado"))

# Desenvolvimento de Gráficos
def grafico_1():
    bplot = plt.boxplot(df_mestrado["Conceito Médio de Mestrado"], patch_artist=True)
    for box in bplot['boxes']:
        box.set(facecolor='blue')
    plt.title("BoxPlot - Conceito Médio de Mestrado")
    plt.xlabel("Mestrado")
    plt.ylabel("Conceito Médio")
    plt.show()

grafico_1()