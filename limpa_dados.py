import pandas as pd

df = pd.read_csv("IGC_2021.csv")
df.fillna(value="-", inplace=True)

# As linhas de indice 2012 e 2013 não contém dados, logo são removidas
df.drop(index=[2012, 2013], inplace = True)

# Corrigindo os nomes das colunas
for column in df.columns:
        if column[0] == " ":
            df[column[1:]] = df[column]
            df.drop(columns=column, inplace=True)

def remove_colunas_sem_dado(df):
    
    for column in df.columns:
        dicionario_value_counts = df[column].value_counts().to_dict()
        
        for key in dicionario_value_counts.keys():
            if key == "-":
                
                num_vazios_da_coluna = dicionario_value_counts[key]
                metade_linhas_df = df.shape[0] / 2

                if num_vazios_da_coluna > metade_linhas_df:
                    df.drop(columns=column, inplace=True)
    return df



