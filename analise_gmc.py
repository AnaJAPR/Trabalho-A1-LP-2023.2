import pandas as pd
import limpa_dados as lp
import func_analises as fan

df1 = fan.media_tres_por_indice(fan.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

def prints_da_analise(df1):
    print("####################### ANÁLISE DOS CONCEITOS #######################", end="\n\n")
    # Vemos no df abaixo as médias dos conceitos médios em cada nível do ensino superior por categoria administrativa
    print(df1, end="\n\n")

    # Vemos a partir da tabela abaixo as categorias administrativas com os maiores Conceitos médios em cada nível de ensino superior
    print(df1[df1 == df1.max()], end="\n\n")
    # A categoria administrativa "Especial" possui a maior média tanto no conceito médio de graduação(3.059135) quanto no do doutorado(4.66137)
    # "Pública Federal" possui a maior média no conceito médio de mestrado(4.3846)

    # Vemos a partir da tabela abaixo as categorias administrativas com os menores Conceitos médios em cada nível de ensino superior
    print(df1[df1 == df1.min()], end="\n\n")
    # A categoria administrativa "Pública Municipal" possui a menor média do conceito médio do doutorado(4.579625)
    # A categoria administrativa "Especial" possui a menor média do conceito médio de mestrado(4)
    # "Pública Federal" possui a menor média no conceito médio de graduação(2.226348)


    # O print abaixo nos revela as médias das 3 colunas
    print(df1.mean(), end="\n\n")
    # Vemos que a maior média é do doutorado e a menor é de graduação

prints_da_analise(df1)

df2 = fan.df[["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado", "Categoria Administrativa"]]
df2 = df2[df2["Conceito Médio de Graduação"] > 0]
df2 = df2[df2["Conceito Médio de Mestrado"] > 0]
df2 = df2[df2["Conceito Médio do doutorado"] > 0]

df2 = df2.set_index("Categoria Administrativa")
#         # # Garantindo que o df esteja tratado
#         # df = lp.corrige_nomes_df(df)
