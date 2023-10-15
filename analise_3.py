import func_analises as fan
import geopandas as gpd
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
# "Mestrado"
df_mestrado = fan.selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
print(df_mestrado, end="\n")
# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_mestrado, "Conceito Médio de Mestrado"))

# Desenvolvimento de Gráficos
def grafico_1():
    bplot = plt.boxplot(df_mestrado["Conceito Médio de Mestrado"], patch_artist=True)
    for box in bplot['boxes']:
            box.set(facecolor="red")
    plt.title("BoxPlot - Conceito Médio de Mestrado")
    plt.xlabel("Mestrado")
    plt.ylabel("Conceito Médio")
    plt.show()

grafico_1()

def grafico_2():
    brasil = gpd.read_file("shapefiles\estados_2010\estados_2010.shp")
    merge = brasil.merge(ocorrencia_por_uf, left_on="sigla", right_on="Sigla da UF", how="left")
    merge.plot(column="count", cmap="viridis", legend=True)
    plt.title("Quantidade de Instituições de Ensino por Estado")
    plt.axis("off")
    plt.show()

grafico_2()
