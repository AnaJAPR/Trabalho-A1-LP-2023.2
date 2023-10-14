import pandas as pd
import doctest

df = pd.read_csv("IGC_2021.csv")

# As linhas de indice 2012 e 2013 não contém dados, logo são removidas
df.drop(index=[2012, 2013], inplace = True)

def remove_colunas_sem_dado(df):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame

        DESCRIPTION. A função confere se há, no DataFrame, alguma coluna onde mais da metade de suas linhas são vazias e, 
        se sim, remove essas colunas.
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna o DataFrame sem as colunas com "muitas células vazias".
    """
    try:
        # Testando se foi passado corretamente um DataFrame como parâmetro
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError
    
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")
    
    else:
        df_sem_vazios = df.fillna(value="-")
        
        for column in df.columns:
            # Cria um dicionário com os valores e quantas vezes eles aparecem na coluna
            dicionario_value_counts = df_sem_vazios[column].value_counts().to_dict()
            
            for key in dicionario_value_counts.keys():
                # Confere a quantidade de células vazias na coluna
                if key == "-":
                    num_vazios_da_coluna = dicionario_value_counts[key]
                    metade_linhas_df = df.shape[0] / 2

                    if num_vazios_da_coluna > metade_linhas_df:
                        # Remove as colunas com mais da metade das células vazias
                        df.drop(columns=column, inplace=True)
    
    finally:
        return df

def trata_celulas_vazias(df):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame

        DESCRIPTION. A função preenche as células vazias do DataFrame:
        As células vazias de colunas não-numéricas são preenchidas com "-";
        Colunas que tem características de booleano, ou seja, possuem apenas (0,1, NA) passaram a ter (False, True, "Sem informações");
        As células vázias das demais colunas numéricas são preenchidas com 0. 
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna o DataFrame sem células vazias.
    """
    try:
        # Testando se foi passado corretamente um DataFrame como parâmetro
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError
    
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")
    
    else:
        # Para esta parte do tratamento, a função vai tratar separadamente as células vazias nas colunas numericas das nas não-numericas
        
        colunas_nao_num = df.select_dtypes(exclude="number").columns

        for coluna in colunas_nao_num:
            df[coluna].fillna(value="-", inplace=True) #Preenche os valores nulos das colunas não-numéricas por "-"
         
        # Nesse passo a função vai conferir se há coluna com características de booleano (0,1)
        df2 = df.fillna(value=0)

        for coluna in df.columns:
            lista_unicos_da_coluna = df2[coluna].unique().tolist()
            
            if lista_unicos_da_coluna.sort() == [0, 1]:
                df2[coluna].astype(bool)
            
            #Troca os valores (0, 1, NA) por (False, True, "Sem informações") 
            if df2[coluna].dtype == bool:
                df[coluna].replace(1, True, inplace=True)
                df[coluna].replace(0, False, inplace=True)
                df[coluna].fillna(value="Sem informações", inplace=True)
        
        # Por fim retorna o DataFrame com as células vazias preenchidas com 0 nas colunas que restam(numéricas)
        df.fillna(value=0, inplace=True)
    
    finally:
        return df
    
def corrige_nomes_df(df):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame

        DESCRIPTION. A função vai utilizar o tratamento feito pelas funções remove_colunas_sem_dado e trata_celulas_vazias.
        Com o DataFrame tratado, ela vai corrigir os nomes nele: nas células e colunas.
        No nome das colunas: remove o espaço antes do nome(se houver); remove o * no fim do nome(se houver).
        Nos nomes nas células: garante que as colunas que possuem siglas, possuam apenas letras maiúsculas; Mantém um padrão
        de escrita com a primeira letra maiúscula e as demais mínusculas em cada palavra.
        
    Returns
    -------
    pandas.core.frame.DataFrame
        Retorna o DataFrame com os nomes corrigidos.

    """
    try:
        # Testando se foi passado corretamente um DataFrame como parâmetro
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError
    
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")
    
    else:
        # Já utilizando o tratamento das demais funções desse módulo
        df = trata_celulas_vazias(remove_colunas_sem_dado(df))
        
        # Corrigindo os nomes das colunas

        # Esse for retira o espaço no início do nome da coluna (se houver)
        for column in df.columns:
                if column[0] == " ":
                    df[column[1:]] = df[column]
                    df.drop(columns=column, inplace=True)
        
        # Esse for retira o * do final do nome da coluna (se houver)
        for new_name_column in df.columns:
                if new_name_column[-1] == "*":
                    nome_sem_asterisco = new_name_column.replace("*", "")
                    df[nome_sem_asterisco] = df[new_name_column]
                    df.drop(columns=new_name_column, inplace=True)

        # Corrigindo strings
        colunas_str = df.select_dtypes(exclude="number").columns

        for coluna in colunas_str:
            for string in df[coluna]:
                
                if string == string.upper():# Garantindo que as siglas se mantenham com letras maiúsculas
                    df[coluna] = df[coluna].str.upper()
                else:
                    df[coluna] = df[coluna].str.title()# Padronizando a escrita dos elementos das demais colunas com strings
    
    finally:    
        return df
    
def media_tres_por_indice(df:pd.core.frame.DataFrame, lista_colunas:list, indice:str):
    """
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        Recebe o DataFrame
    lista_colunas : list
        Recebe uma lista com exatamente os nomes de 3 colunas nunéricas do DataFrame
    filtro : str
        Uma string de um nome de uma coluna não-numérica

        DESCRIPTION. A função recebe um DataFrame e garante que ele esteja tratado (executando a função corrige_nomes_df) e retorna
        um DataFrame com a coluna escolhida em "indice" como indice, colunas com a media dos dados não nulos das escolhidas
        em "lista_colunas" por cada registro do "indice".
        
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
        # Garantindo que o df esteja tratado
        df = corrige_nomes_df(df)
        
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

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-trata_celulas_vazias.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-remove_colunas_sem_dado.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-corrige_nomes_df.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-media_tres_por_indice.txt", verbose=True)
