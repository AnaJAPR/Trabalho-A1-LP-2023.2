import pandas as pd
import limpa_dados as lp

df1 = lp.media_tres_por_indice(lp.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

# Vemos a partir da tabela abaixo as categorias administrativas com os maiores Conceitos médios em cada nível de ensino superior
print(df1[df1 == df1.max()])
# A categoria administrativa "Especial" possui a maior média tanto no conceito médio de graduação(3.059135) quanto no do doutorado(4.66137)
# "Pública Federal" possui a maior média no conceito médio de mestrado(4.3846)
print(df1.mean())

