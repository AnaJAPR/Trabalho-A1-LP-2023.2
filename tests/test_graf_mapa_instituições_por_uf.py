import sys
sys.path.append('.')
import unittest
from unittest.mock import Mock, patch
from analise_paulo import graf_mapa_instituições_por_uf, df
import pandas as pd

class GrafMapaInstituicoesPorUF(unittest.TestCase):
    def teste_com_df_e_colunas(self):
    # Cria um Mock para plt.show() para evitar que o gráfico seja exibido
        mock_show = Mock()
        with patch('matplotlib.pyplot.show', mock_show):
            resultado = graf_mapa_instituições_por_uf(df, "shapefiles\estados_2010\estados_2010.shp")
    # A função não possui retorno, apenas gera o gráfico
        self.assertIsNone(resultado)

    def teste_sem_df_existente(self):
        resultado = graf_mapa_instituições_por_uf("Não sou um df", "shapefiles\estados_2010\estados_2010.shp")
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_df_sem_colunas_necessarias(self):
        resultado = graf_mapa_instituições_por_uf(df, 29)
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_coluna_nao_esta_no_df(self):
        resultado = graf_mapa_instituições_por_uf(df.drop("Sigla da UF", axis=1), "shapefiles\estados_2010\estados_2010.shp")
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_coluna_uf_numerica(self):
        resultado = graf_mapa_instituições_por_uf(pd.DataFrame({"Sigla da UF":[4, 3, 2, 1]}), "shapefiles\estados_2010\estados_2010.shp")
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_com_df_e_colunas(self):
        resultado = graf_mapa_instituições_por_uf(df, "shapefiles\estados_2010\inexistente.shp")
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()