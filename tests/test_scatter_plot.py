import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
from unittest.mock import Mock, patch
from func_analises import df, reindexacao_e_filtragem
from analise_guilherme import scatter_plot

class TestReindexacaoEFiltragem(unittest.TestCase):
    # teste com parâmetro válido
    def test_scatter_plot_com_dataframe(self):
        
        # Cria um Mock para plt.show() para evitar que o gráfico seja exibido
        mock_show = Mock()
        with patch('matplotlib.pyplot.show', mock_show):
        # Chama a função a ser testada
            resultado = scatter_plot(df, reindexacao_e_filtragem(df, "Conceito Médio de Graduação"), 
                                     reindexacao_e_filtragem(df, "Conceito Médio de Mestrado"),
                                     reindexacao_e_filtragem(df, "Conceito Médio do doutorado"))

            # Adiciona as asserções apropriadas para verificar o resultado
            self.assertIsNone(resultado) # A função não deve retornar nada

    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_scatter_plot_sem_receber_dfs_em_todos_parametros(self):
        
        resultado = scatter_plot(df, "Tio Rafa", "abobrinha", 42)

        # Conferindo se ela não retorna nada com o erro
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = scatter_plot()
        
        self.assertEqual(str(cm.exception), "scatter_plot() missing 4 required positional arguments: 'df', 'df_grad', 'df_mest', and 'df_dout'")

if __name__ == "__main__":
    unittest.main()