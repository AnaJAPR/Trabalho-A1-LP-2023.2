import limpa_dados as lp
import pandas as pd
from dominate import document
from dominate.tags import h1, img
# import analise_ana as aa
import analise_paulo as ap
# import analise_Otavio as ao
import analise_guilherme as ag

#ao.analise_org_media_num_cursos(df)
#ao.analise_org_num_catadm_empilhado(df)
#ao.analise_intervalos_igc_catadm_pizza(df)

# Gráficos de Ana
# aa.cria_plot_1_ana(aa.analise_1_ana(df))
# aa.cria_plot_2_ana(aa.analise_ana_2(aa.analise_1_ana(df)))

# Gráficos do Paulo
ap.graf_boxplot_conceito_medio_mestrado()
ap.graf_mapa_instituições_por_uf()
ap.graf_hist_alfa_beta_gama()

# Gráficos do Guilherme
ag.grafico_medias_cm()

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