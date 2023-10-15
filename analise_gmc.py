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

def prints_de_todas_medianas(df1):
    print(df1)
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
            
            if not df_mest["Conceito Médio de Mestrado"].loc[cat_adm].shape[0] == 1: 
                mediana_mest = df_mest.loc[cat_adm].median()
            else:
                mediana_mest = df_mest["Conceito Médio de Mestrado"].loc[cat_adm]

        if cat_adm in df_dout.index:
            
            if not df_dout["Conceito Médio do doutorado"].loc[cat_adm].shape[0] == 1:
                mediana_dout = df_dout.loc[cat_adm].median()
            else:
                mediana_dout = df_dout["Conceito Médio do doutorado"].loc[cat_adm]

        # Vemos a seguir as medianas por cada dos CMs por cada categoria
        print(f"A mediana do CM de graduação na categoria {cat_adm} é {mediana_grad}")
        print(f"A mediana do CM de mestrado na categoria {cat_adm} é {mediana_mest}")
        print(f"A mediana do CM do doutorado na categoria {cat_adm} é {mediana_dout}", end="\n\n")
            

df2 = fan.media_tres_por_indice(fan.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

def prints_da_analise_das_medias(df2):
    print("####################### ANÁLISE DAS MÉDIAS DOS CONCEITOS MÉDIOS#######################", end="\n\n")
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
    boxplot = plt.boxplot(df2, patch_artist=True)

    for box in boxplot["boxes"]:
            box.set(facecolor="blue")
    
    plt.title("BoxPlot - Comparação da média do Conceito Médio")
    plt.xlabel("Níveis do ensino superior")
    plt.ylabel("Conceito Médio")
    plt.show()

grafico_medias_cm()