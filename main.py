import pandas as pd
from dominate import document
from dominate.tags import h1, img
import limpa_dados as lp
import func_analises as fan
# import analise_ana as aa
import analise_paulo as ap
import analise_otavio as ao
import analise_guilherme as ag

# Cria DataFrame
df = pd.read_csv("IGC_2021.csv")

# As linhas de indice 2012 e 2013 não contém dados, logo são removidas
df.drop(index=[2012, 2013], inplace = True)

# Limpa os Dados
df = lp.corrige_nomes_df(df)

print(df.columns)

# Gerando os Dataframes filtrados para Conceitos Médios de cada um dos níveis de ensino para as plotagens do Guilherme
df_grad = fan.reindexacao_e_filtragem(df, "Conceito Médio de Graduação")
df_mest = fan.reindexacao_e_filtragem(df, "Conceito Médio de Mestrado")
df_dout = fan.reindexacao_e_filtragem(df, "Conceito Médio do doutorado")

df_conc_medios = fan.media_tres_por_indice(df, ["Conceito Médio de Graduação", "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

# Gráficos do Otavio
ao.analise_org_media_num_cursos(df)
ao.analise_org_num_catadm_empilhado(df)
ao.analise_intervalos_igc_catadm_pizza(df)

# Gráficos de Ana
# aa.cria_plot_1_ana(aa.analise_1_ana(df))
# aa.cria_plot_2_ana(aa.analise_ana_2(aa.analise_1_ana(df)))

# Gráficos do Paulo
ap.graf_boxplot_conceito_medio_mestrado(df)
ap.graf_mapa_instituições_por_uf(df, "shapefiles/estados_2010/estados_2010.shp")
ap.graf_hist_alfa_beta_gama(df)

# Gráficos do Guilherme
ag.grafico_medias_cm(df_conc_medios)
ag.scatter_plot(df_grad, df_mest, df_dout)
# ag.prints_da_analise_das_medias(df_conc_medios)

doc = document(title="Meus Gráficos")

with doc:
     h1("Gráfico 1")
     img(src="graphic_folder/grafico_1.png")
     
     h1("Gráfico 2")
     img(src="graphic_folder/grafico_2.png")
     
     h1("Gráfico 3")
     img(src="graphic_folder/grafico_3.png")
    
     h1("Gráfico 4")
     img(src="graphic_folder/grafico_4.png")

     h1("Gráfico 5")
     img(src="graphic_folder/grafico_5.png")

     h1("Gráfico 6")
     img(src="graphic_folder/grafico_6.png")

# Salva a página HTML em um arquivo
with open("index.html", "w") as f:
    f.write(doc.render())