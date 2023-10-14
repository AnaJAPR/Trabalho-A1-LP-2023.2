import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt
import doctest

df = lp.corrige_nomes_df(lp.df)

def selecionar_colunas_eliminando_nulos(df:pd.core.frame.DataFrame, colunas:list):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Recebe um DataFrame.
    colunas : list
        Recebe uma lista de colunas pertencentes ao DataFrame.

        DESCRIPTION. A função tem como objetivo selecionar um determinado conjunto de
        colunas de um DataFrame e remover todas as linhas tais que a primeira coluna
        possua valor igual a 0 ou nulo.
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna um DataFrame contendo as 3 colunas passadas. Em caso de erro, o DataFrame
        passado como argumento será retornado sem nenhuma alteração.

    """
    try:
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError("O argumento passado não é um DataFrame Pandas.")
        if type(colunas) != list:
            raise TypeError("O argumento passado não é uma lista.")
        if not set(colunas) <= set(df.columns):
            raise NameError("Uma ou mais colunas passadas não estão presentes no DataFrame.")
    except TypeError:
        new_df = df
        print("Um ou mais argumentos passados não corresponde ao tipo solicitado.")
    except NameError:
        new_df = df
        print("Uma ou mais colunas passadas não estão presentes no DataFrame.")
    else:
        new_df = df[colunas].astype(float)
        new_df = new_df[(new_df[colunas[0]] != 0) & (new_df[colunas[0]].notna())]
    finally:
        return new_df

# # Análise "Instituições de Ensino por UF"
# sigla_uf = df["Sigla da UF"]
# print(sigla_uf, end="\n")

# ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
# print(ocorrencia_por_uf, end="\n")

# # Análise "Conceito Médio de Mestrado"
# df_mestrado = selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
# print(df_mestrado, end="\n")

# Medidas de tendência central e dispersão
# mestrado_conceito_medio_media = df_mestrado["Conceito Médio de Mestrado"].mean()
# print("Média de Conceito Médio de Mestrado: ", mestrado_conceito_medio_media, end="\n")

# mestrado_conceito_medio_mediana = df_mestrado["Conceito Médio de Mestrado"].median()
# print("Mediana de Conceito Médio de Mestrado: ", mestrado_conceito_medio_mediana, end="\n")

# mestrado_conceito_medio_std = df_mestrado["Conceito Médio de Mestrado"].std()
# print("Desvio Padrão de Conceito Médio de Mestrada: ", mestrado_conceito_medio_std, end="\n")

# mestrado_conceito_medio_max = df_mestrado["Conceito Médio de Mestrado"].max()
# print("Conceito Médio de Mestrado Máximo: ", mestrado_conceito_medio_max, end="\n") 

# mestrado_conceito_medio_min = df_mestrado["Conceito Médio de Mestrado"].min()
# print("Conceito Médio de Mestrado Mínimo: ", mestrado_conceito_medio_min, end="\n")

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-selecionar_colunas_eliminando_nulos.txt", verbose=True)