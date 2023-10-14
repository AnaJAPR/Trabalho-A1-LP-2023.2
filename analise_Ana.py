import limpa_dados as lp
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o df limpo. Usei apenas uma função de lp porque ela já possui as outras dentro dela
df = lp.corrige_nomes_df(lp.df)

def analise_1_ana(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    
        DESCRIPTION. A função verifica quais são os valores únicos da coluna "Organização Acadêmica" e, então, 
        faz um dicionário com a frequência de ocorrência de cada IGC faixa para cada "organização Acadêmica".
        
    Returns
    -------
    dict
        Retorna um dicionário cujas chaves são valores únicos de "Organização Acadêmica" e cujos valores são dicionários
        os quais apresentam dados de IGC faixa como chave e a frequência de ocorrência destes para sua respectiva 
        organização acadêmica como valores.
    """
    
    # Criando uma lista com os valores únicos da coluna "Organização Acadêmica"
    valores_unicos_org_acad = df["Organização Acadêmica"].unique().tolist()

    # Criando lista onde serão colocados os dicionários advindos do for abaixo
    dic_cont_IGC_faixa_por_org_acad = list()

    # Criando dicionários, cada um referente a um valor único da coluna "Organização Acadêmica"
    # As chaves de cada dicionário se referem aos dados de "IGC (Faixa)" e os valores são frequências de ocorrência de cada faixa para cada org_acad
    for org_acad in valores_unicos_org_acad:
        dic_contagem_IGC_faixa = df[df["Organização Acadêmica"] == org_acad]["IGC (Faixa)"].value_counts().to_dict()
        dic_cont_IGC_faixa_por_org_acad.append(dic_contagem_IGC_faixa)

    # Elaborando o dicionário final, com os dicionários anteriores sendo valores agora e as chaves sendo a respectiva org_acad de cada um    
    tupla_org_acad_e_dic_IGC_faixa = zip(valores_unicos_org_acad, dic_cont_IGC_faixa_por_org_acad)
    dicionario_final = dict(tupla_org_acad_e_dic_IGC_faixa)
    
    return dicionario_final

def analise_ana_2(dicionario_final):
    """
    Parameters
    ----------
    dicionario_final: dict
    
        DESCRIPTION. A função itera sobre os elementos do dicionario_final, assumindo que este é o mesmo dicionário retornado pela
        função analise_1_ana, ou seja, assumimos que os valores desse dicionário são dicionários também, cujas chaves são valores,
        em sua maioria, números em formato string. Então, a função procura a média de IGC Faixa por Organização Acadêmica, fazendo 
        o produto das chaves (após transformá-las em int) pelas seus valores (frequência de ocorrência de cada) e dividindo pela
        soma das contagens.
    
    Returns
    -------
    dict
        Retorna um dicionário cujas chaves são os valores únicos de "Organização Acadêmica" e cujos valores são a média de IGC faixa
        referente a cada chave.
    """
    
    media_por_org_acad = {}

    # Itera sobre chaves e valores de dicionario_final (o que a função analise_1_ana retorna a partir do df limpo)
    for org_acad, contagens in dicionario_final.items():
        total_contagens = sum(contagens.values())
        soma = 0
        
        # Itera sobre os elementos dos dicionários que são valores de dicionario_final
        for chave, contagem in contagens.items():
            try:
                chave_numerica = int(chave)
                soma += chave_numerica * contagem
            # se não tiver como transformar em int, continua lendo o código
            except ValueError:
                continue
        # Para garantir que não vai ter divisões por zero, o if analise se o número de contagens é positivo.
        if total_contagens > 0:
            media = soma/total_contagens
        else:
            media = 0
        
        # Adicionando as chaves e os valores do dicionário media_por_org_acad
        media_por_org_acad[org_acad] = media
        # Deixando as médias com até três casas decimais
        media_arredondada = {chave: round(valor, 3) for chave, valor in media_por_org_acad.items()}
        
    return media_arredondada

def cria_plot_1_ana(dicionario_contagem):
    # Converte o dicionário em um DataFrame do pandas
    df = pd.DataFrame.from_dict(dicionario_contagem, orient='index')

    # Classifica o DataFrame com base nas colunas (IGC Faixa)
    df = df.sort_index(axis=1)
    
    # Define o estilo do gráfico
    plt.style.use("seaborn-darkgrid")
    
    for org_acad in df.index:
        igc_faixas = df.columns
        frequencias = df.loc[org_acad].values
        plt.plot(igc_faixas, frequencias, label=org_acad, marker="o", linestyle="--", markersize=6)

    plt.xlabel("IGC Faixa", size=15, color="green", alpha=0.5)
    plt.ylabel("Frequência de Ocorrência", size=15, color="green", alpha=0.5)
    plt.title("Frequência de Ocorrência de cada IGC Faixa por Organização Acadêmica", size=20, color="purple", alpha=0.7)
    plt.legend(loc="upper left", fontsize = 7)
    plt.show()
    
dicionario_contagem = analise_1_ana(df)
cria_plot_1_ana(dicionario_contagem)
