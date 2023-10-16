import doctest
import func_analises as fan
import geopandas as gpd
import limpa_dados as lp
import matplotlib.pyplot as plt
import os
import pandas as pd

df = fan.df

# Desenvolvimento de Gráficos
# Conceito Médio de Mestrado
def graf_boxplot_conceito_medio_mestrado(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame 

        DESCRIPTION. A função extrai as colunas "Beta (Proporção de Mestrado - Equivalente)" 
        e "Conceito Médio de Mestrado" do DataFrame de modo a remover todas as linhas vazias.
        Em seguida é criado um boxplot.

    Returns
    -------
    None
        A função somente exibe o gráfico criado e o salva em um arquivo na pasta "graphic_folder"
    """
    try:
        if not type(df) == pd.core.frame.DataFrame:
            raise TypeError("O argumento passado não é um DataFrame.")
        if not set(["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"]) <= set(df.columns):
            raise NameError("O DataFrame necessita conter as colunas 'Beta (Proporção de Mestrado - Equivalente)' e 'Conceito Médio de Mestrado'.")
        if not pd.api.types.is_numeric_dtype(df["Beta (Proporção de Mestrado - Equivalente)"]) or not pd.api.types.is_numeric_dtype(df["Conceito Médio de Mestrado"]):
            raise ValueError("As colunas 'Beta (Proporção de Mestrado - Equivalente)' e 'Conceito Médio de Mestrado' necessitam ser numéricas.")
    except TypeError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except NameError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except ValueError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    
    else:
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

        plt.savefig("graphic_folder/grafico_03.png")
        plt.show()

# INSTITUIÇÕES DE ENSINO POR UF
def graf_mapa_instituições_por_uf(df, path_shapefile):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    path_shapefile: str

        DESCRIPTION. A função extrai a coluna "Sigla da UF" e cálculo quantas vezes cada
        valor aparece. O shapefile dado como argumento é passado e, juntamente com a
        informação da contagem é criado um gráfico de mapa.
        
    Returns
    -------
    None
        A função somente exibe o gráfico criado e o salva em um arquivo na pasta "graphic_folder"
    """
    try:
        if not type(df) == pd.core.frame.DataFrame:
            raise TypeError("O argumento passado não é um DataFrame.")
        if not type(path_shapefile) == str:
            raise TypeError("O argumento passado não é uma string.")
        if not "Sigla da UF" in df.columns:
            raise NameError("O DataFrame necessita conter a coluna 'Sigla da UF'.")
        if pd.api.types.is_numeric_dtype(df["Sigla da UF"]):
            raise ValueError("A coluna 'Sigla da UF' não deve ser numérica.")
        if not os.path.exists(path_shapefile):
            raise FileNotFoundError("O shapefile não foi encontrado.")
    except TypeError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except NameError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except ValueError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except FileNotFoundError as erro:
        print(f"{erro.__class__.__name__}: {erro}")

    else:
        # Extraindo a coluna "Sigla da UF" e realizando value_counts()
        sigla_uf = df["Sigla da UF"]
        ocorrencia_por_uf = sigla_uf.value_counts().to_frame()

        # Utilizando um shapefile para o desenvolvimento de um gráfico de mapa
        brasil = gpd.read_file(path_shapefile)
        merge = brasil.merge(ocorrencia_por_uf, left_on="sigla", right_on="Sigla da UF", how="left")
        merge.plot(column="count", cmap="viridis", legend=True)

        # Personalizando o gráfico
        plt.title("Quantidade de Instituições de Ensino por Estado")
        plt.axis("off")

        plt.savefig("graphic_folder/grafico_04.png")
        plt.show()

# ALFA, BETA E GAMA
def graf_hist_alfa_beta_gama(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame

        DESCRIPTION. A função extrai as colunas de proporção de graduação, mestrado e doutorado
        Com elas é criado um gráfico contendo um histograma para cada uma das colunas.
        
    Returns
    -------
    None
        A função somente exibe o gráfico criado e o salva em um arquivo na pasta "graphic_folder"
    """
    try:
        if not type(df) == pd.core.frame.DataFrame:
            raise TypeError("O argumento passado não é um DataFrame.")
        if not set(["Alfa (Proporção de Graduação)", "Beta (Proporção de Mestrado - Equivalente)", "Gama (Proporção de Doutorandos – Equivalente)"]) <= set(df.columns):
            raise NameError("O DataFrame necessita conter as colunas 'Alfa (Proporção de Graduação)', 'Beta (Proporção de Mestrado - Equivalente)' e 'Gama (Proporção de Doutorandos – Equivalente)'.")
        if pd.api.types.is_numeric_dtype(df["Alfa (Proporção de Graduação)"]) == False or pd.api.types.is_numeric_dtype(df["Beta (Proporção de Mestrado - Equivalente)"]) == False or pd.api.types.is_numeric_dtype(df["Gama (Proporção de Doutorandos – Equivalente)"]) == False:
            raise ValueError("As colunas 'Alfa (Proporção de Graduação)', 'Beta (Proporção de Mestrado - Equivalente)' e 'Gama (Proporção de Doutorandos – Equivalente)' necessitam ser numéricas.")
    
    except TypeError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except NameError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    except ValueError as erro:
        print(f"{erro.__class__.__name__}: {erro}")
    else:
        # Extraindo as colunas
        df_alfa_beta_gama = df[["Alfa (Proporção de Graduação)", "Beta (Proporção de Mestrado - Equivalente)", "Gama (Proporção de Doutorandos – Equivalente)"]]

        # Criando cada um dos subgráficos
        fig, axs = plt.subplots(1, 3, figsize=(12, 4))
        axs[0].hist(df_alfa_beta_gama["Alfa (Proporção de Graduação)"], bins=10, color="#008B00")
        axs[1].hist(df_alfa_beta_gama["Beta (Proporção de Mestrado - Equivalente)"], bins=10, color="#8B0000")
        axs[2].hist(df_alfa_beta_gama["Gama (Proporção de Doutorandos – Equivalente)"], bins=10, color="#00008B")
    
        # Personalizando o grádico de graduação
        axs[0].set_title("Proporção de Graduação")
        axs[0].set_xlim(0, 1)
        axs[0].set_xlabel("Proporção")
        axs[0].set_ylabel("Número de Instituições de Ensino")

        # Personalizando o gráfico de mestrado
        axs[1].set_title("Proporção de Mestrado")
        axs[1].set_xlim(0, 1)
        axs[1].set_xlabel("Proporção")

        # Personalizando o gráfico de doutorado
        axs[2].set_title("Proporção de Doutorado")
        axs[2].set_xlim(0, 1)
        axs[2].set_xlabel("Proporção")

        plt.tight_layout()

        plt.savefig("graphic_folder/grafico_05.png")
        plt.show()

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-graf_boxplot_conceito_medio_mestrado.txt")
    doctest.testfile("doctest_folder\doctest-graf_mapa_instituições_por_uf.txt")
    doctest.testfile("doctest_folder\doctest-graf_hist_alfa_beta_gama.txt")