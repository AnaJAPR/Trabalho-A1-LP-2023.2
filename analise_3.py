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

def medidas_tendencia_e_dispersao(df:pd.core.frame.DataFrame, coluna:str):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Recebe um DataFrame.
    coluna : str
        Recebe uma string que representa o nome de uma coluna do DataFrame.

        DESCRIPTION. A função analisa uma coluna do DataFrame e extrai as informações
        de média, mediana, desvio padrão, máximo e mínimo.
        
    Returns
    -------
    dict
        Retorna um dicionário contendo a medida resumo ou de dispersão como chave e o
        seu valor como valor.

    """
    try:
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError("O argumento passado não é um DataFrame Pandas.")
        if type(coluna) != str:
            raise TypeError("O argumento passado não é uma string.")
        if not coluna in df.columns:
            raise NameError("A coluna passada não está presente no DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[coluna]):
            raise ValueError("A coluna passada não é numérica.")
    except TypeError as erro:
        return str(erro)
    except NameError as erro:
        return str(erro)
    except ValueError as erro:
        return str(erro)
    else:
        media = df[coluna].mean()
        mediana = df[coluna].median()
        desvio_padrao = df[coluna].std()
        maximo = df[coluna].max()
        minimo = df[coluna].min()
    resumo = {"Média":media,
              "Mediana":mediana,
              "Desvio Padrão": desvio_padrao,
              "Máximo": maximo,
              "Mínimo": minimo}
    return resumo

# Análise "Instituições de Ensino por UF"
sigla_uf = df["Sigla da UF"]
print(sigla_uf, end="\n")

ocorrencia_por_uf = sigla_uf.value_counts().to_frame()
print(ocorrencia_por_uf, end="\n")

# Análise "Conceito Médio de Mestrado"
df_mestrado = selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
print(df_mestrado, end="\n")

# Medidas de tendência central e dispersão
print(medidas_tendencia_e_dispersao(df_mestrado, "Conceito Médio de Mestrado"))

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-selecionar_colunas_eliminando_nulos.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-medidas_tendencia_e_dispersao.txt", verbose=True)