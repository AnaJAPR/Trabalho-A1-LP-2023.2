import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Analise 1
def analise_org_media_num_cursos(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame 
        colunas: "Organização Acadêmica", "Nº de Cursos com CPC no triênio"

        DESCRIPTION. A função calcula a média do número de cursos por tipo de Organização Acadêmica e cria
        um grafico de colunas com eixo-x sendo o tipo da Organização e eixo-y a média.
        
    Returns
    -------
    None
        Apenas cria o gráfico de média de cursos com organização acadêmica.
    """
    
    # Teste para que argumento passado seja DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Argumento passado tem que se DataFrame")
    
    # Teste para que DataFrame contenha colunas necessárias
    colunas_necessarias = ["Organização Acadêmica", "Nº de Cursos com CPC no triênio"]
    if not all(column in df.columns for column in colunas_necessarias):
        raise ValueError("DataFrame deve conter colunas: 'Organização Acadêmica' e 'Nº de Cursos com CPC no triênio'.")
        
    # Teste para que colunas tenham dados dos tipos corretos
    if df["Organização Acadêmica"].dtype != "object" or df["Categoria Administrativa"].dtype != "object":
        raise ValueError("Colunas 'Organização Acadêmica' e 'Categoria Administrativa' devem conter tipo string")    
        
    # Os dados_1 representam a agrupação das Organizações Academicas com a média do numero de cursos já calculada.
    dados_1 = df.groupby("Organização Acadêmica")["Nº de Cursos com CPC no triênio"].mean()

    # Usamos dados_1 para criar o grafico_1 com titulo
    grafico_1 = dados_1.plot(kind="bar", xlabel="Organização Acadêmica", ylabel="Média de Número de Cursos")
    plt.title("Número de Cursos por Organização Acadêmica")
    
    # Calculamos a média arredondada e adiconamos essa no grafico_1 posicionado acima das colunas
    for indice, elemento in enumerate(dados_1):
        grafico_1.text(indice, elemento, round(elemento, 2), ha="center", va="bottom")

    plt.savefig("graphic_folder/grafico_08.png")
    plt.show()
    


# Analise 2
def analise_org_num_catadm_empilhado(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame 
        colunas: "Organização Acadêmica", "Categoria Administrativa", "Código da IES"

        DESCRIPTION. A função calcula a quantidade de instituições para cada Organização Acadêmica, e quantas de cada das
        Categorias Administrativas compôe esse tipo de organização. Esses dados são grafados num gráfico de colunas
        empilhadas.
        Também é calculado para cada tipo de Oganização Acadêmica qual Categoria Administrativa é mais presente
        em sua composição, a quantidade desta categoria e a porcentagem que representa. Esses resultados são printados.

    Returns
    -------
    None
        Apenas cria o gráfico e printa os dados adicionais.
    """

        
    # Teste para que argumento passado seja DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Argumento passado tem que se DataFrame")
        
    # Teste para que DataFrame contenha colunas necessárias
    colunas_necessarias = ["Organização Acadêmica", "Categoria Administrativa", "Código da IES"]
    if not all(column in df.columns for column in colunas_necessarias):
        raise ValueError("DataFrame deve conter colunas: 'Organização Acadêmica', 'Categoria Administrativa' e 'Código da IES'.")
        
    # Teste para que colunas tenham dados dos tipos corretos
    if df["Organização Acadêmica"].dtype != "object" or df["Categoria Administrativa"].dtype != "object" or df["Código da IES"].dtype != "float64":
        raise ValueError("Colunas 'Organização Acadêmica' e 'Categoria Administrativa' devem conter tipo string e 'Código da IES' tipo float.")
        

    # Os dados_2 representam as organizações relacionadas a categorias, para cada unica instituição
    dados_2 = df.groupby(["Organização Acadêmica", "Categoria Administrativa"])["Código da IES"].count().unstack()

    # Grafo_2 utiliza stacked para empilhar em cada org as categorias que a compõe
    grafo_2 = dados_2.plot(kind="bar", stacked=True, figsize=(10, 5))

    # Calculamos o total de instituições em cada tipo de organização, convertemos em int e posicionamos acima das colunas
    for indice, valor in enumerate(dados_2.sum(axis=1)):
        grafo_2.text(indice, valor, f"Total: {int(valor)}", ha="center", va="bottom")
    
    # Criamos duas variáveis para sabermos qual categoria é mais representada em um tipo de org, e calculamos do total de instituições nesse org a porcentagem que essa categoria representa.
    mais_representada = dados_2.idxmax(axis=1)
    porcentagem_mais_representada = (dados_2.max(axis=1) / dados_2.sum(axis=1) * 100).round(2)

    # Utilizamos as variaveis para printar os resultados [ara cada tipo de Organização]:
    for i, org in enumerate(dados_2.index):
        print(f"{org}:")
    
        print(f"   Categoria Administrativa mais representada: {mais_representada[i]}")
    
        numero_mais_representada = dados_2.loc[org][mais_representada[i]]
        print(f"   Número de {mais_representada[i]} nessa organização: {int(numero_mais_representada)}")
    
        print(f"   Porcentagem nessa organização: {porcentagem_mais_representada[i]}%\n")

    plt.xlabel("Organização Acadêmica")
    plt.ylabel("Número de Instituições")
    plt.title("Número de Instistuições por tipo de organização e categoria administrativa")
    # Ancoramos a legenda de forma que não cubra o grafico.
    plt.legend(title="Categoria Administrativa", bbox_to_anchor=(1, 1), loc="upper left")
    plt.savefig("graphic_folder/grafico_09.png")
    plt.show()




# Analise 3
def analise_intervalos_igc_catadm_pizza(df):
    """
    Parameters
    ----------
    df: pandas.core.frame.DataFrame 
        colunas: "Categoria Administrativa", "IGC (Contínuo)"
    
        DESCRIPTION. A função calcula o valor de certos percentuais do IGC (Contínuo) - um float entre 0 e 5 -
        nos valores de 15%, 50% e 85%. Utilizando esses valores, define um intervalo e calcula as Categorias Administrativas o
        que representam. Depois, cria um grafico de pizza para cada intervalo que mostra a composição do intervalo por Categoria Administrativa.

    Returns
    -------
    None
        Apenas cria o gráfico de pizza.
    """ 
    
    # Teste para que argumento passado seja DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Argumento passado tem que se DataFrame")
    
    # Teste para que DataFrame contenha colunas necessárias
    colunas_necessarias = ["Categoria Administrativa", "IGC (Contínuo)"]
    if not all(column in df.columns for column in colunas_necessarias):
        raise ValueError("DataFrame deve conter colunas: 'Categoria Administrativa' e 'IGC (Contínuo)'.")
        
    # Teste para que colunas tenham dados dos tipos corretos
    if df["Categoria Administrativa"].dtype != "object" or df["IGC (Contínuo)"].dtype != "float64":
        raise ValueError("Coluna 'Categoria Administrativa' deve conter tipo string e 'IGC (Contínuo)' tipo float.")
        

    # Usamos a funçao de numpy para achar os valores de IGC correspondentes aos percentuais
    igc_intervalo = np.percentile(df["IGC (Contínuo)"], [15, 50, 85])

    # Criamos a df para os Intervalos do IGC seguindo os valores dos percentuais calculados, com os intervalos sendo de 0-15%, 15%-50%, 50%-85%, 85%-100%
    df["IGC Intervalo"] = pd.cut(df["IGC (Contínuo)"], bins=[0, igc_intervalo[0], igc_intervalo[1], igc_intervalo[2], df["IGC (Contínuo)"].max()], labels=["Menor 15%", "Menor 50%", "Maior 50%", "Maior 15%"])


    # Calculamos a quantidade com value_counts() de cada Categoria Administrativa para cada Intervalo de IGC.
    # 4 vezes para cada intervalo definido pelo nome:
        
    # Max 15%
    max_15_df = df[df["IGC Intervalo"] == "Maior 15%"]
    categoria_max_15 = max_15_df["Categoria Administrativa"].value_counts()

    # Min 15%
    min_15_df = df[df["IGC Intervalo"] == "Menor 15%"]
    categoria_min_15 = min_15_df["Categoria Administrativa"].value_counts()

    # 50 a 85%
    max_50a85_df = df[df["IGC Intervalo"] == "Maior 50%"]
    categoria_max_50a85 = max_50a85_df["Categoria Administrativa"].value_counts()

    # 15 a 50%
    min_15a50_df = df[df["IGC Intervalo"] == "Menor 50%"]
    categoria_min_15a50 = min_15a50_df["Categoria Administrativa"].value_counts()



    # Para formamos uma só imagem com os 4 graficos, definimos uma grade de 2x2 para posicionar as pizzas
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Primeiro crimanos o titulo para um setor, em seguida a pizza com .pie e os dados de quantidade de Categoria no intervalo"
    # O final incluí a porcentagem de cada categoria como float. Isso se repete para todos os intervalos.
    # Max 15%
    axes[0, 0].set_title("Maior 15% IGC - Categoria Administrativa")
    axes[0, 0].pie(categoria_max_15, labels=categoria_max_15.index, autopct="%1.1f%%")
    
    # Min 15%
    axes[0, 1].set_title("Menor 15% IGC - Categoria Administrativa")
    axes[0, 1].pie(categoria_min_15, labels=categoria_min_15.index, autopct="%1.1f%%")
    
    # 50 a 85%
    axes[1, 0].set_title("50% a Maior 15% IGC - Categoria Administrativa")
    axes[1, 0].pie(categoria_max_50a85, labels=categoria_max_50a85.index, autopct="%1.1f%%")
    
    # 15 a 50%
    axes[1, 1].set_title("50% a Menor 15% IGC - Categoria Administrativa")
    axes[1, 1].pie(categoria_min_15a50, labels=categoria_min_15a50.index, autopct="%1.1f%%")
    
    plt.savefig("graphic_folder/grafico_10.png")
    plt.show()
