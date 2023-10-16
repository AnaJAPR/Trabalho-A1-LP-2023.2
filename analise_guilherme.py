import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import func_analises as fan
import doctest
import func_analises as fan

# Coloquei os prints em uma função apenas para não poluir a main toda vez que roda-la, e só aparecerem caso chamada sua função

def prints_da_analise_das_medias(df:pd.core.frame.DataFrame):
    """
    Parameters
    ----------
    df : pd.core.frame.DataFrame
        Recebe o dataframe gerado

        DESCRIPTION. A função printa análises de um DataFrame com colunas "Média Conceito Médio de Graduação", "Média Conceito Médio de Mestrado", 
        "Média Conceito Médio do doutorado" por indices("Categoria Administrativa").
        
    Returns
    -------
    NoneType
        Retorna apenas os prints da análise.
    """
    try:
        if type(df) != pd.core.frame.DataFrame:
            raise TypeError
        if df.equals(fan.media_tres_por_indice(fan.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado",
                                                                 "Conceito Médio do doutorado"], "Categoria Administrativa")) == False:
            raise ValueError
                         
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")

    except ValueError:
        print(f"ValueError: O parâmetro df não está no formato necessário!")

    else:
        print("####################### ANÁLISE DAS MÉDIAS DOS CONCEITOS MÉDIOS #######################", end="\n\n")
        # Vemos no df abaixo as médias dos conceitos médios em cada nível do ensino superior por categoria administrativa
        print(df, end="\n\n")

        # Vemos a partir da tabela abaixo as categorias administrativas com os maiores Conceitos médios em cada nível de ensino superior
        print(df[df == df.max()], end="\n\n")
        # A categoria administrativa "Especial" possui a maior média tanto no conceito médio de graduação(3.059135) quanto no do doutorado(4.66137)
        # "Pública Federal" possui a maior média no conceito médio de mestrado(4.3846)

        # Vemos a partir da tabela abaixo as categorias administrativas com os menores Conceitos médios em cada nível de ensino superior
        print(df[df == df.min()], end="\n\n")
        # A categoria administrativa "Pública Municipal" possui a menor média do conceito médio do doutorado(4.579625)
        # A categoria administrativa "Especial" possui a menor média do conceito médio de mestrado(4)
        # "Pública Federal" possui a menor média no conceito médio de graduação(2.226348)


        # O print abaixo nos revela as médias das 3 colunas
        print("AS médias de cada nível de ensino são: ", df.mean(), sep="\n", end="\n\n")
        # Vemos que a maior média é do doutorado(4.628627) e a menor é de graduação(2.573522)

        # O print abaixo nos revela as medianas das 3 colunas
        print("AS medianas de cada nível de ensino são: ", df.median(), sep="\n", end="\n\n")
        # O maior valor novamente é do doutorado(4.64235) e o menor e da graduação(2.525514)

        # A partir das medidas de resumo acima, vemos que a mediana e a média são muito proximas em seus respectivos níveis de graduação
        # Vemos também que o mestrado se mantém bem próximo do doutorado e distante da graduação nas notas (sua média é 4.267921 e sua mediana é 4.304046)

        # O print abaixo dos da o desvioo padrão das médias
        print("O devio padrão em cada nível de ensino são: ", df.std(), sep="\n", end="\n\n")
        # O maior desvio é da graduação(0.293501) e o menor o do doutorado(0.036502). O desvio padrão das médias do mestrado é 0.137659

def grafico_medias_cm(df, df_conc_medios):
    """
    Parameters
    ----------
    df : pd.core.frame.DataFrame
        Recebe o DataFrame principal 
    df_conc_medios : pd.core.frame.DataFrame
        Recebe o DataFrame gerado por fan.media_tres_por_indice(df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")
       
        DESCRIPTION. Recebe o DataFrame "df" para tratamento. O gráfico é um Boxplot gerado pelo DataFrame df_conc_medios. 
        
    Returns
    -------
    NoneType
        Apenas plota e salva o gráfico.
    """
    try:
        if type(df) != pd.core.frame.DataFrame or type(df_conc_medios) != pd.core.frame.DataFrame:
            raise TypeError
    
        if df_conc_medios.equals(fan.media_tres_por_indice(df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado",
                                                                 "Conceito Médio do doutorado"], "Categoria Administrativa")) == False:
             raise ValueError
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")
    except ValueError:
        print(f"ValueError: O parâmetro df_conc_medios não está no formato necessário!")
    else:
        # Criando o boxplot
        boxplot = plt.boxplot(df_conc_medios, patch_artist=True)

        # Alterando a cor das caixas do boxplot
        for box in boxplot["boxes"]:
                box.set(facecolor="blue")

        # Nomeando
        plt.xticks([1, 2, 3], ["Graduação", "Mestrado", "Doutorado"])
        plt.title("BoxPlot - Comparação da média por categoria do Conceito Médio")
        plt.xlabel("Níveis do ensino superior")
        plt.ylabel("Conceito Médio")

        # Salvando e plotando
        plt.savefig("graphic_folder/grafico_06.png")
        plt.show()


def scatter_plot(df,df_grad, df_mest, df_dout):
    """
    Parameters
    ----------
    df : pd.core.frame.DataFrame
        Recebe o DataFrame principal 
    df_grad : pd.core.frame.DataFrame
        Recebe o DataFrame gerado por fan.reindexacao_e_filtragem(df, "Conceito Médio de Graduação")
    df_mest : pd.core.frame.DataFrame
        Recebe o DataFrame gerado por fan.fan.reindexacao_e_filtragem(df, "Conceito Médio de Mestrado")
    df_dout : pd.core.frame.DataFrame
        Recebe o DataFrame gerado por fan.fan.reindexacao_e_filtragem(df, "Conceito Médio do doutorado")

        DESCRIPTION. Recebe o DataFrame "df" para tratamento. O gráfico é um Scatterplot gerado pelos DataFrame df_grad,
        df_mest e df_dout. 
        
    Returns
    -------
    NoneType
        Apenas plota e salva o gráfico.
    """
    try:
        if type(df) != pd.core.frame.DataFrame or type(df_grad) != pd.core.frame.DataFrame or type(df_mest) != pd.core.frame.DataFrame or type(df_dout) != pd.core.frame.DataFrame:
            raise TypeError
        
        if not df_grad.equals(fan.reindexacao_e_filtragem(df, "Conceito Médio de Graduação")):
            erro = "df_grad"
            raise ValueError
        
        if not df_mest.equals(fan.reindexacao_e_filtragem(df, "Conceito Médio de Mestrado")):
            erro = "df_mest"
            raise ValueError
        
        if not df_dout.equals(fan.reindexacao_e_filtragem(df, "Conceito Médio do doutorado")):
            erro = "df_dout"
            raise ValueError
    
    except TypeError:
        print("TypeError: A função só pode receber DataFrame!")
    except ValueError:
        print(f"ValueError: O parâmetro {erro} não está no formato necessário!")
    else:

        # Convertendo as categorias em números
        df_grad.index = pd.Categorical(df_grad.index)
        df_grad.index = df_grad.index.codes

        df_mest.index = pd.Categorical(df_mest.index)
        df_mest.index = df_mest.index.codes

        df_dout.index = pd.Categorical(df_dout.index)
        df_dout.index = df_dout.index.codes

        # Fazendo o jitter para diminuir as sobreposições
        grad_index_jitted = df_grad.index.tolist() + np.random.normal(-0.1, 0.1, len(df_grad.index.tolist()))
        mest_index_jitted = df_mest.index.tolist() + np.random.normal(-0.1, 0.1, len(df_mest.index.tolist()))
        dout_index_jitted = df_dout.index.tolist() + np.random.normal(-0.1, 0.1, len(df_dout.index.tolist()))

        # Criando o gráfico de dispersão com os Conceitos Médios dos 3 níveis de ensino superior nas cores dos pontos
        plt.scatter(x=grad_index_jitted, y=df_grad, color="yellow", alpha=0.5)
        plt.scatter(x=mest_index_jitted, y=df_mest, color="green", alpha=0.5)
        plt.scatter(x=dout_index_jitted, y=df_dout, color="blue", alpha=0.5)

        plt.xticks([0, 1, 2, 3, 4, 5], ["Especial", "Priv. C/ Fins Lucrativos", "Priv. S/ Fins Lucrativos",
                                        "Pública Estadual", "Pública Federal", "Pública Municipal"], rotation=15)

        # Adicionando legenda ao gráfico
        legend_elements = [plt.Line2D([0], [0], marker="o", color="white", label="Conceito Médio de Graduação",
                            markerfacecolor="yellow", markersize=10),
                        plt.Line2D([0], [0], marker="o", color="white", label="Conceito Médio de Mestrado",
                            markerfacecolor="green", markersize=10),
                        plt.Line2D([0], [0], marker="o", color="white", label="Conceito Médio do doutorado",
                            markerfacecolor="blue", markersize=10)]
        plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc="lower right")

        # Salvando e plotando
        plt.savefig("graphic_folder/grafico_07.png")
        plt.show()

if __name__ == "__main__":
    doctest.testfile("doctest_folder\doctest-prints_da_analise_das_medias.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-grafico_medias_cm.txt", verbose=True)
    doctest.testfile("doctest_folder\doctest-scatter_plot.txt", verbose=True)