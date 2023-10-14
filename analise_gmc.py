import pandas as pd
import limpa_dados as lp
import func_analises as fan

df1 = fan.df[["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado", "Categoria Administrativa"]]
df1 = df1[df1["Conceito Médio de Graduação"] > 0]
df1 = df1[df1["Conceito Médio de Mestrado"] > 0]
df1 = df1[df1["Conceito Médio do doutorado"] > 0]

df1 = df1.set_index("Categoria Administrativa")

def prints_da_analise_geral(df1):
    pass


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




