import limpa_dados as ld
import pandas as pd
import matplotlib.pyplot as plt

# definindo o df com as alterações do limpa_dados
df = ld.df

# Deixando como padrão letras minúsculas na coluna "Organização Acadêmica*"
# Isso porque nela há "FACULDADE" e "faculdade" e eu preciso que o python entenda ambos como iguais. 

df["Organização Acadêmica*"] = df["Organização Acadêmica*"].str.lower()

# Filtrando quais os dados da coluna "Organização Acadêmica"
tipos_org_acad = df["Organização Acadêmica*"].unique().tolist()
print(tipos_org_acad)


