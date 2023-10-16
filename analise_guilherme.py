import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import func_analises as fan

df1 = fan.df[["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado", "Categoria Administrativa"]]
df_grad = df1[df1["Conceito Médio de Graduação"] > 0][["Conceito Médio de Graduação", "Categoria Administrativa"]]
df_mest = df1[df1["Conceito Médio de Mestrado"] > 0][["Conceito Médio de Mestrado", "Categoria Administrativa"]]
df_dout = df1[df1["Conceito Médio do doutorado"] > 0][["Conceito Médio do doutorado", "Categoria Administrativa"]]

df1 = df1.set_index("Categoria Administrativa")
df_grad = df_grad.set_index("Categoria Administrativa")
df_mest = df_mest.set_index("Categoria Administrativa")
df_dout = df_dout.set_index("Categoria Administrativa")

# Coloquei os prints em funções apenas para não poluírem a main toda vez que roda-la

def prints_de_todas_medianas():
    """
    Parameters
    ----------
    None

        DESCRIPTION. A função printa as medianas das colunas "Conceito Médio de Graduação", "Conceito Médio de Mestrado", 
        "Conceito Médio do doutorado" por indices("Categoria Administrativa").
        
    Returns
    -------
    None
        Retorna apenas os prints das medianas.
    """ 
    indices = fan.df["Categoria Administrativa"].unique().tolist()
    
    mediana_grad, mediana_mest, mediana_dout = 0,0,0
    
    # Exibe as medianas dos Conceitos Médios nas respectivas Categorias Administrativa
    for cat_adm in indices:

        if cat_adm in df_grad.index:# Conferindo se há o nível de ensino no respectivo curso
            
            if not df_grad.loc[cat_adm].shape[0] == 1:# O caso de um unico registro será tratado separadamente
                mediana_grad = df_grad["Conceito Médio de Graduação"].loc[cat_adm].median()# Pegando a mediana
            
            else:# Caso só haja um registro, ele é a pópria mediana
                mediana_grad = df_grad["Conceito Médio de Graduação"].loc[cat_adm]
    
    # O que valeu para o if acima vale pros demais 
        if cat_adm in df_mest.index:
            
            if not df_mest.loc[cat_adm].shape[0] == 1: 
                mediana_mest = df_mest["Conceito Médio de Mestrado"].loc[cat_adm].median()
            else:
                mediana_mest = df_mest["Conceito Médio de Mestrado"].loc[cat_adm]

        if cat_adm in df_dout.index:
            
            if not df_dout.loc[cat_adm].shape[0] == 1:
                mediana_dout = df_dout["Conceito Médio do doutorado"].loc[cat_adm].median()
            else:
                mediana_dout = df_dout["Conceito Médio do doutorado"].loc[cat_adm]

        # Vemos a seguir as medianas por cada dos CMs por cada categoria
        print(f"A mediana do CM de graduação na categoria {cat_adm} é {mediana_grad}")
        print(f"A mediana do CM de mestrado na categoria {cat_adm} é {mediana_mest}")
        print(f"A mediana do CM do doutorado na categoria {cat_adm} é {mediana_dout}", end="\n\n")  

df2 = fan.media_tres_por_indice(fan.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

def prints_da_analise_das_medias():
    """
    Parameters
    ----------
    None

        DESCRIPTION. A função printa análises de um DataFrame com colunas "Média Conceito Médio de Graduação", "Média Conceito Médio de Mestrado", 
        "Média Conceito Médio do doutorado" por indices("Categoria Administrativa").
        
    Returns
    -------
    None
        Retorna apenas os prints da análise.
    """
    print("####################### ANÁLISE DAS MÉDIAS DOS CONCEITOS MÉDIOS #######################", end="\n\n")
    # Vemos no df abaixo as médias dos conceitos médios em cada nível do ensino superior por categoria administrativa
    print(df2, end="\n\n")

    # Vemos a partir da tabela abaixo as categorias administrativas com os maiores Conceitos médios em cada nível de ensino superior
    print(df2[df2 == df2.max()], end="\n\n")
    # A categoria administrativa "Especial" possui a maior média tanto no conceito médio de graduação(3.059135) quanto no do doutorado(4.66137)
    # "Pública Federal" possui a maior média no conceito médio de mestrado(4.3846)

    # Vemos a partir da tabela abaixo as categorias administrativas com os menores Conceitos médios em cada nível de ensino superior
    print(df2[df2 == df2.min()], end="\n\n")
    # A categoria administrativa "Pública Municipal" possui a menor média do conceito médio do doutorado(4.579625)
    # A categoria administrativa "Especial" possui a menor média do conceito médio de mestrado(4)
    # "Pública Federal" possui a menor média no conceito médio de graduação(2.226348)


    # O print abaixo nos revela as médias das 3 colunas
    print("AS médias de cada nível de ensino são: ", df2.mean(), sep="\n", end="\n\n")
    # Vemos que a maior média é do doutorado(4.628627) e a menor é de graduação(2.573522)

    # O print abaixo nos revela as medianas das 3 colunas
    print("AS medianas de cada nível de ensino são: ", df2.median(), sep="\n", end="\n\n")
    # O maior valor novamente é do doutorado(4.64235) e o menor e da graduação(2.525514)

    # A partir das medidas de resumo acima, vemos que a mediana e a média são muito proximas em seus respectivos níveis de graduação
    # Vemos também que o mestrado se mantém bem próximo do doutorado e distante da graduação nas notas (sua média é 4.267921 e sua mediana é 4.304046)

    # O print abaixo dos da o desvioo padrão das médias
    print("O devio padrão em cada nível de ensino são: ", df2.std(), sep="\n", end="\n\n")
    # O maior desvio é da graduação(0.293501) e o menor o do doutorado(0.036502). O desvio padrão das médias do mestrado é 0.137659


def grafico_medias_cm():
    # Criando o boxplot
    boxplot = plt.boxplot(df2, patch_artist=True)

    # Alterando a cor das caixas do boxplot
    for box in boxplot["boxes"]:
            box.set(facecolor="blue")

    # Nomeando
    plt.xticks([1, 2, 3], ["Graduação", "Mestrado", "Doutorado"])
    plt.title("BoxPlot - Comparação da média por categoria do Conceito Médio")
    plt.xlabel("Níveis do ensino superior")
    plt.ylabel("Conceito Médio")

    # Salvando e plotando
    plt.savefig("graphic_folder/grafico_6.png")
    plt.show()


def scatter_plot(df_graduacao, df_mestrado, df_doutorado):
    # Crie um DataFrame com as colunas e índices desejados
    data = {'Conceito Médio de Graduação': df_graduacao,
            'Conceito Médio de Mestrado': df_mestrado,
            'Conceito Médio do doutorado': df_doutorado}
    # df = pd.DataFrame(data, index=['Pública Federal', 'Pública Estadual', 'Privada Sem Fins Lucrativos', 'Especial', 'Pública Municipal', 'Privada Com Fins Lucrativos'])

    # Convertendo as categorias em números
    df_grad.index = pd.Categorical(df_graduacao.index)
    df_grad.index = df_grad.index.codes

    df_mest.index = pd.Categorical(df_mestrado.index)
    df_mest.index = df_mest.index.codes

    df_dout.index = pd.Categorical(df_doutorado.index)
    df_dout.index = df_dout.index.codes

    grad_index_jitted = df_grad.index.tolist() + np.random.normal(-0.1, 0.1, len(df_grad.index.tolist()))
    mest_index_jitted = df_mest.index.tolist() + np.random.normal(-0.1, 0.1, len(df_mest.index.tolist()))
    dout_index_jitted = df_dout.index.tolist() + np.random.normal(-0.1, 0.1, len(df_dout.index.tolist()))

    # Crie o gráfico de dispersão com subcategorias nas cores dos pontos
    plt.scatter(x=grad_index_jitted, y=df_grad, c='yellow', alpha=0.5)
    plt.scatter(x=mest_index_jitted, y=df_mest, c='green', alpha=0.5)
    plt.scatter(x=dout_index_jitted, y=df_dout, c='blue', alpha=0.5)

    # plt.xticks([0, 1, 2, 3, 4, 5], df_grad.index)

    # Adicione uma legenda ao gráfico
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Conceito Médio de Graduação',
                          markerfacecolor='yellow', markersize=10),
                    plt.Line2D([0], [0], marker='o', color='w', label='Conceito Médio de Mestrado',
                          markerfacecolor='green', markersize=10),
                    plt.Line2D([0], [0], marker='o', color='w', label='Conceito Médio do doutorado',
                          markerfacecolor='blue', markersize=10)]
    plt.legend(handles=legend_elements)

    # Exiba o gráfico
    plt.show()

scatter_plot(df_grad, df_mest, df_dout)