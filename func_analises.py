import doctest
import pandas as pd
import limpa_dados as lp

df = lp.corrige_nomes_df(lp.df)

def selecionar_colunas_eliminando_nulos(df:pd.core.frame.DataFrame, colunas:list):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
        Recebe um DataFrame.
    colunas: list
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
        # Testando possíveis erros ao passar o argumento
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
        # Selecionando as colunas do DataFrame como float
        new_df = df[colunas].astype(float)
        # Eliminando todas as ocorrências de "0" ou "NA"
        new_df = new_df[(new_df[colunas[0]] != 0) & (new_df[colunas[0]].notna())]
    finally:
        return new_df
    
def medidas_tendencia_e_dispersao(df:pd.core.frame.DataFrame, coluna:str):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
        Recebe um DataFrame.
    coluna: str
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
        # Testando possíveis erros para os argumentos da função
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
        # Calculando medidas resumos e adicionando-as à um dicionário a ser retornado
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

def media_tres_por_indice(df:pd.core.frame.DataFrame, lista_colunas:list, indice:str):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    lista_colunas: list
    filtro : str

        DESCRIPTION. A função recebe um DataFrame tratado e retorna um DataFrame com a coluna escolhida em "indice"
        como indice, colunas com a media dos dados não nulos das escolhidas em "lista_colunas" por cada registro do "indice".
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna um DataFrame com index=indice, colunas=lista_colunas e os dados vão ser as 
        médias dos dados não nulos das colunas escolhidas do DataFrame original.
    """
    try:
        # Testando se foi passado corretamente um DataFrame como parâmetro
        if not type(df) == pd.core.frame.DataFrame or not type(lista_colunas) == list or not type(indice) == str:
            raise TypeError
        # Testando se lista_colunas foi passado com o n° correto de elementos
        if not len(lista_colunas) == 3:
            raise ValueError("A lista deve conter 3 elementos!")
        
        for elemento in lista_colunas:
            if elemento not in df.columns:
                raise ValueError(f"O nome da coluna foi escrito errado em '{elemento}'!")
        
        if indice not in df.columns:
            raise ValueError("O nome escolhido para indice não é o nome de uma coluna do DataFrame!")
        
    except TypeError:
        print("TypeError: A função tem que receber um Dataframe, uma lista e uma string!")

    else:
        df_filtrado = df[[indice, lista_colunas[0], lista_colunas[1], lista_colunas[2]]]

        # Retirando os 0, pois não serão úteis para esta análise
        df_filtrado1 = df_filtrado[df_filtrado[lista_colunas[0]] > 0]
        df_filtrado2 = df_filtrado[df_filtrado[lista_colunas[1]] > 0]
        df_filtrado3 = df_filtrado[df_filtrado[lista_colunas[2]] > 0]

        lista_registros = df_filtrado[indice].unique().tolist()
        
        dic_medias = dict()
        for registro in lista_registros:
            
            media_registro_1 = df_filtrado1[df_filtrado1[indice] == registro][lista_colunas[0]].mean()
            media_registro_2 = df_filtrado2[df_filtrado2[indice] == registro][lista_colunas[1]].mean()
            media_registro_3 = df_filtrado3[df_filtrado3[indice] == registro][lista_colunas[2]].mean()
            medias = [media_registro_1, media_registro_2, media_registro_3]
            dic_medias[registro] = medias

        colunas = ["Média " + lista_colunas[0], "Média " + lista_colunas[1], "Média " + lista_colunas[2]]
        dados = list()
        
        for valor in dic_medias.values():
            dados.append(valor)

        df_medias = pd.DataFrame(dados, index=sorted(dic_medias.keys()), columns=colunas)

        # Caso aconteça algum erro de aparecer valores NaN no df final:
        for coluna in df_medias:
            for index in lista_registros:#Pegando os indices do df_medias
                    
                    # Substituindo os NaN por "-" para facillitar o tratamento
                    df_medias.fillna("-", inplace=True)
                    if df_medias[coluna].loc[index] == "-":# Localizando onde estaria o NaN

                        if coluna == "Média " + lista_colunas[0] or coluna == "Média " + lista_colunas[1] or coluna == "Média " + lista_colunas[2]:
                            nome_coluna = coluna[6:]# Pegando o nome da coluna no df original

                        # Executando novamente o que ocorre no for que calcula as médias
                        df_medias[coluna].loc[index] = df_filtrado3[df_filtrado3[indice] == index][nome_coluna].mean()

        return df_medias

def reindexacao_e_filtragem(df, coluna):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
        Recebe um Dataframe de ICG
    coluna: str
        Recebe uma coluna de Conceito Médio 

        DESCRIPTION. A função cria um DataFrame a partir da coluna selecionada sem valores nulos, 
        com um novo índice.
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna um DataFrame apenas com a coluna selecionada e índice "Categoria Administrativa".
    """ 
    try:
        if type(df) != pd.core.frame.DataFrame:
            erro = "df"
            tipo = "um DataFrame"
            raise TypeError
        
        if type(coluna) != str:
            erro = "coluna"
            tipo = "uma string"
            raise TypeError
    
        if df.equals(df = lp.corrige_nomes_df(lp.df)) == False:
             raise ValueError
        
        if coluna not in df.columns.tolist():
            raise NameError
        
        if "Categoria Administrativa" not in df.columns.tolist():
            raise ValueError
        
    except TypeError:
        print(f"TypeError: O parâmetro {erro} deve ser {tipo}!")

    except ValueError:
        print("ValueError: O DataFrame passado não está no formato necessário!")

    except NameError:
        print(f"{coluna} não é uma coluna do DataFrame passado!")

    else:
        new_df = df[df[coluna] > 0][[coluna, "Categoria Administrativa"]]

        new_df = new_df.set_index("Categoria Administrativa")

        return new_df

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-selecionar_colunas_eliminando_nulos.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-medidas_tendencia_e_dispersao.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-media_tres_por_indice.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-reindexacao_e_filtragem.txt", verbose=True)
