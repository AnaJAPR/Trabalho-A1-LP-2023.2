import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o df limpo. Usei apenas uma função de lp porque ela já possui as outras dentro dela
df = lp.corrige_nomes_df(lp.df)

def analise_1_ana(df):
    # Criando uma lista com os valores únicos da coluna "Organização Acadêmica"
    valores_unicos_org_acad = df["Organização Acadêmica"].unique().tolist()

    # Criando uma lista com os valores únicos da coluna "IGC (Faixa)"
    # valores_unicos_IGC_faixa = df["IGC (Faixa)"].unique().tolist()

    dic_cont_IGC_faixa_por_org_acad = list()

    # Adicionando dicionários, cada um referente a um valor único da coluna "Organização Acadêmica".
    # As chaves de cada dicionário se referem aos dados de "IGC (Faixa)" e os valores são frequências de ocorência de cada faixa para cada org_acad
    for org_acad in valores_unicos_org_acad:
        dic_contagem_IGC_faixa = df[df["Organização Acadêmica"] == org_acad]["IGC (Faixa)"].value_counts().to_dict()
        dic_cont_IGC_faixa_por_org_acad.append(dic_contagem_IGC_faixa)

    # Elaborando o dicionário final, com os dicionários anteriores sendo valores agora e as chaves sendo a respectiva org_acad de cada um    
    tupla_org_acad_e_dic_IGC_faixa = zip(valores_unicos_org_acad, dic_cont_IGC_faixa_por_org_acad)
    dicionario_final = dict(tupla_org_acad_e_dic_IGC_faixa)
    
    return dicionario_final

def analise_ana_2(dicionario_final):
    media_por_org_acad = {}
    
    for org_acad, contagens in dicionario_final.items():
        total_contagens = sum(contagens.values())
        soma = 0
        
        for chave, contagem in contagens.items():
            try:
                chave_numerica = int(chave)
                soma += chave_numerica * contagem
            except ValueError:
                continue
            
        if total_contagens > 0:
            media = soma/total_contagens
        else:
            media = 0
        
        media_por_org_acad[org_acad] = media
        media_arredondada = {chave: round(valor, 3) for chave, valor in media_por_org_acad.items()}
        
    return media_arredondada

# print(analise_ana_2(analise_1_ana(df)))

def cria_plot_1_ana(dicionario_contagem):
    # Converte o dicionário em um DataFrame do pandas
    df = pd.DataFrame.from_dict(dicionario_contagem, orient='index')

    # Classifica o DataFrame com base nas colunas (IGC Faixa)
    df = df.sort_index(axis=1)
    
    # Define o estilo do gráfico
    plt.style.use("seaborn-darkgrid")
    
    fig, ax = plt.subplots()
    
    for org_acad in df.index:
        igc_faixas = df.columns
        frequencias = df.loc[org_acad].values
        ax.scatter(igc_faixas, frequencias, label=org_acad, marker="o")

    ax.set_xlabel("IGC (Faixa)")
    ax.set_ylabel("Frequência de Ocorrência")
    ax.set_title("Frequência de Ocorrência de cada IGC Faixa por Organização Acadêmica")
    ax.legend()
    plt.show()
    
dicionario_contagem = analise_1_ana(df)
cria_plot_1_ana(dicionario_contagem)