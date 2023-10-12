import pandas as pd
import doctest

df = pd.read_csv("IGC_2021.csv")

# As linhas de indice 2012 e 2013 não contém dados, logo são removidas
df.drop(index=[2012, 2013], inplace = True)

# Corrigindo os nomes das colunas
for column in df.columns:
        if column[0] == " ":
            df[column[1:]] = df[column]
            df.drop(columns=column, inplace=True)

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

if __name__ == "__main__":
    doctest.testfile("doctest-trata_celulas_vazias.txt", verbose=True)
    doctest.testfile("doctest-remove_colunas_sem_dado.txt", verbose=True)