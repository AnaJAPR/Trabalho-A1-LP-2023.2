import limpa_dados as ld
import pandas as pd
import matplotlib.pyplot as plt

# definindo o df com as alterações do limpa_dados
df = ld.df

# Deixando como padrão letras minúsculas na coluna "Organização Acadêmica*"
# Isso porque nela há "FACULDADE" e "faculdade" e eu preciso que o python entenda ambos como iguais. 

df["Organização Acadêmica*"] = df["Organização Acadêmica*"].str.lower()

# Criando uma lista com os valores únicos da coluna "Organização Acadêmica"
valores_unicos_org_acad = df["Organização Acadêmica*"].unique().tolist()
# print(valores_unicos_org_acad)

# Criando uma lista com os valores únicos da coluna "IGC (Faixa)"
valores_unicos_IGC_faixa = df["IGC (Faixa)"].unique().tolist()
# print(valores_unicos_IGC_faixa)

#rascunho em desenvolvimento
for org_acad in valores_unicos_org_acad:
    media_IGC_faixa = df[df["Organização Acadêmica*"] == org_acad]["IGC (Faixa)"].mean()
    chave_valor = {org_acad: media_IGC_faixa}
    print(chave_valor)
    


