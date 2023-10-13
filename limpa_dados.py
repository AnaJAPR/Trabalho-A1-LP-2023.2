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

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-trata_celulas_vazias.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-remove_colunas_sem_dado.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-corrige_nomes_df.txt", verbose=True)
