import sys
sys.path.append('.')
import unittest
from unittest.mock import Mock, patch
from analise_paulo import graf_boxplot_conceito_medio_mestrado, df
import pandas as pd

class GrafBoxplotConceitoMedioMestrado(unittest.TestCase):
    def teste_com_df_e_colunas(self):
    # Cria um Mock para plt.show() para evitar que o gráfico seja exibido
        mock_show = Mock()
        with patch('matplotlib.pyplot.show', mock_show):
            resultado = graf_boxplot_conceito_medio_mestrado(df)
    # A função não possui retorno, apenas gera o gráfico
        self.assertIsNone(resultado)

    def teste_sem_df_existente(self):
        resultado = graf_boxplot_conceito_medio_mestrado("Não sou um df")
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_df_sem_colunas_necessarias(self):
        resultado = graf_boxplot_conceito_medio_mestrado(df.drop("Beta (Proporção de Mestrado - Equivalente)", axis=1))
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

    def teste_coluna_nao_esta_no_df(self):
        resultado = graf_boxplot_conceito_medio_mestrado(pd.DataFrame({"Beta (Proporção de Mestrado - Equivalente)":df["Beta (Proporção de Mestrado - Equivalente)"].astype(str), "Conceito Médio de Mestrado":df["Conceito Médio de Mestrado"].astype(str)}))
    # Checa se o retorno foi nulo (O gráfico foi gerado ou houve um erro tratado)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()