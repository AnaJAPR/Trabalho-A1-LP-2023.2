import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o df limpo. Usei apenas uma função de lp porque ela já possui as outras dentro dela
df = lp.corrige_nomes_df(lp.df)

# Criando uma lista com os valores únicos da coluna "Organização Acadêmica"
valores_unicos_org_acad = df["Organização Acadêmica"].unique().tolist()
print(valores_unicos_org_acad)

# Criando uma lista com os valores únicos da coluna "IGC (Faixa)"
valores_unicos_IGC_faixa = df["IGC (Faixa)"].unique().tolist()
print(valores_unicos_IGC_faixa)

dic_cont_IGC_faixa_por_org_acad = list()

# Adicionando dicionários, cada um referente a um valor único da coluna "Organização Acadêmica".
# As chaves de cada dicionário se referem a um valor de "IGC (Faixa)" e os valores são frequências de ocorência de cada faixa para cada org_acad
for org_acad in valores_unicos_org_acad:
    dic_contagem_IGC_faixa = df[df["Organização Acadêmica"] == org_acad]["IGC (Faixa)"].value_counts().to_dict()
    dic_cont_IGC_faixa_por_org_acad.append(dic_contagem_IGC_faixa)

# Elaborando o dicionário final, com os dicionários anteriores sendo valores agora e as chaves sendo a respectiva org_acad de cada um    
tupla_org_acad_e_dic_IGC_faixa = zip(valores_unicos_org_acad, dic_cont_IGC_faixa_por_org_acad)
dicionario_final = dict(tupla_org_acad_e_dic_IGC_faixa)
print(dicionario_final)

