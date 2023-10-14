import pandas as pd
import limpa_dados as lp

df1 = lp.media_tres_por_indice(lp.df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Sigla da UF")