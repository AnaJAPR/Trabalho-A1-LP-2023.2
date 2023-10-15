import limpa_dados as lp
import pandas as pd
#import analise_Otavio as ao
# import analise_Ana as aa

df = pd.read_csv("IGC_2021.csv")

df = lp.corrige_nomes_df(lp.df)

#ao.analise_org_media_num_cursos(df)
#ao.analise_org_num_catadm_empilhado(df)
#ao.analise_intervalos_igc_catadm_pizza(df)

# aa.cria_plot_1_ana(aa.analise_1_ana(df))
# aa.cria_plot_2_ana(aa.analise_ana_2(aa.analise_1_ana(df)))