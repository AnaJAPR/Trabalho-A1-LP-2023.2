import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

# definindo o df com as alterações do limpa_dados
df = lp.corrige_nomes_df(lp.df)

# Criando uma lista com os valores únicos da coluna "Organização Acadêmica"
valores_unicos_org_acad = df["Organização Acadêmica"].unique().tolist()
print(valores_unicos_org_acad)

# Criando uma lista com os valores únicos da coluna "IGC (Faixa)"
valores_unicos_IGC_faixa = df["IGC (Faixa)"].unique().tolist()
print(valores_unicos_IGC_faixa)

lista_de_dicionarios = list()
#rascunho em desenvolvimento
for org_acad in valores_unicos_org_acad:
    contagem_IGC_faixa = df[df["Organização Acadêmica"] == org_acad]["IGC (Faixa)"].value_counts().to_dict()
    lista_de_dicionarios.append(contagem_IGC_faixa)
    
pares = zip(valores_unicos_org_acad, lista_de_dicionarios)
dicionario = dict(pares)
print(dicionario)
    
# print(lista_de_dicionarios)

    


