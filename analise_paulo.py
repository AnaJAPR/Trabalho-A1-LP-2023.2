import func_analises as fan
import geopandas as gpd
import limpa_dados as lp
import matplotlib.pyplot as plt
import pandas as pd

# Desenvolvimento de Gráficos
# CONCEITO MÉDIO DE MESTRADO
def graf_boxplot_conceito_medio_mestrado(df):
    # Selecionando as colunas de "Beta" e "Conceito de Mestrado"
    df_mestrado = fan.selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
    bplot = plt.boxplot(df_mestrado["Conceito Médio de Mestrado"], patch_artist=True)
    
    # Personalizando o BoxPlot
    for box in bplot['boxes']:
        box.set(facecolor="#8B0000")
    plt.title("BoxPlot - Conceito Médio de Mestrado")
    plt.xlabel("Mestrado")
    plt.ylabel("Conceito Médio")
    plt.gca().set_xticklabels([])

    plt.savefig("graphic_folder/grafico_3.png")
    plt.show()

# INSTITUIÇÕES DE ENSINO POR UF
def graf_mapa_instituições_por_uf(df):
    # Extraindo a coluna "Sigla da UF" e realizando value_counts()
    sigla_uf = df["Sigla da UF"]
    ocorrencia_por_uf = sigla_uf.value_counts().to_frame()

    # Utilizando um shapefile para o desenvolvimento de um gráfico de mapa
    brasil = gpd.read_file("shapefiles\estados_2010\estados_2010.shp")
    merge = brasil.merge(ocorrencia_por_uf, left_on="sigla", right_on="Sigla da UF", how="left")
    merge.plot(column="count", cmap="viridis", legend=True)

    # Personalizando o gráfico
    plt.title("Quantidade de Instituições de Ensino por Estado")
    plt.axis("off")

    plt.savefig("graphic_folder/grafico_4.png")
    plt.show()

# ALFA, BETA E GAMA
def graf_hist_alfa_beta_gama(df):
    df_alfa_beta_gama = df[["Alfa (Proporção de Graduação)", "Beta (Proporção de Mestrado - Equivalente)", "Gama (Proporção de Doutorandos – Equivalente)"]]
    df_alfa_beta_gama["Soma"] = df_alfa_beta_gama["Alfa (Proporção de Graduação)"] + df_alfa_beta_gama["Beta (Proporção de Mestrado - Equivalente)"] + df_alfa_beta_gama["Gama (Proporção de Doutorandos – Equivalente)"]

    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].hist(df_alfa_beta_gama["Alfa (Proporção de Graduação)"], bins=10, color="#008B00")
    axs[0].set_title("Proporção de Graduação")
    axs[0].set_xlim(0, 1)
    axs[0].set_xlabel("Proporção")
    axs[0].set_ylabel("Número de Instituições de Ensino")

    axs[1].hist(df_alfa_beta_gama["Beta (Proporção de Mestrado - Equivalente)"], bins=10, color="#8B0000")
    axs[1].set_title("Proporção de Mestrado")
    axs[1].set_xlim(0, 1)
    axs[1].set_xlabel("Proporção")

    axs[2].hist(df_alfa_beta_gama["Gama (Proporção de Doutorandos – Equivalente)"], bins=10, color="#00008B")
    axs[2].set_title("Proporção de Doutorado")
    axs[2].set_xlim(0, 1)
    axs[2].set_xlabel("Proporção")

    plt.tight_layout()

    plt.savefig("graphic_folder/grafico_5.png")
    plt.show()