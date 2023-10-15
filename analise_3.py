import func_analises as fan
import geopandas as gpd
import limpa_dados as lp
import matplotlib.pyplot as plt
import pandas as pd

df = lp.corrige_nomes_df(lp.df)

# ANÁLISE - INSTITUIÇÕES DE ENSINO POR UF
# Extraindo a coluna "Sigla da UF"
sigla_uf = df["Sigla da UF"]
print(sigla_uf, end="\n")

# Observando número de ocorrências por UF
ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
print(ocorrencia_por_uf, end="\n")

# ANÁLISE - CONCEITO MÉDIO DE MESTRADO
# Selecionando as colunas de "Beta" e "Conceito de Mestrado"
df_mestrado = fan.selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
print(df_mestrado, end="\n")

# Medidas de tendência central e dispersão
print(fan.medidas_tendencia_e_dispersao(df_mestrado, "Conceito Médio de Mestrado"))

# Desenvolvimento de Gráficos
def grafico_1():
    bplot = plt.boxplot(df_mestrado["Conceito Médio de Mestrado"], patch_artist=True)
    
    # Personalizando o BoxPlot
    for box in bplot['boxes']:
            box.set(facecolor="red")
    plt.title("BoxPlot - Conceito Médio de Mestrado")
    plt.xlabel("Mestrado")
    plt.ylabel("Conceito Médio")
    plt.show()

grafico_1()

def grafico_2():
    # Utilizando um shapefile para o desenvolvimento de um gráfico de mapa
    brasil = gpd.read_file("shapefiles\estados_2010\estados_2010.shp")
    merge = brasil.merge(ocorrencia_por_uf, left_on="sigla", right_on="Sigla da UF", how="left")
    merge.plot(column="count", cmap="viridis", legend=True)

    # Personalizando o gráfico
    plt.title("Quantidade de Instituições de Ensino por Estado")
    plt.axis("off")
    plt.show()

grafico_2()
