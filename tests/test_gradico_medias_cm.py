import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
from unittest.mock import Mock, patch
from func_analises import df, media_tres_por_indice
from analise_guilherme import grafico_medias_cm

class TestReindexacaoEFiltragem(unittest.TestCase):
    # teste com parâmetro válido
    def test_grafico_medias_cm_com_dataframe(self):
        
        # Cria um Mock para plt.show() para evitar que o gráfico seja exibido
        mock_show = Mock()
        with patch('matplotlib.pyplot.show', mock_show):
        # Chama a função a ser testada
            resultado = grafico_medias_cm(df, media_tres_por_indice(df, ["Conceito Médio de Graduação", 
                                                                         "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa"))

            # Adiciona as asserções apropriadas para verificar o resultado
            self.assertIsNone(resultado) # A função não deve retornar nada

    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_grafico_medias_cm_sem_receber_os_dois_dfs(self):
        
        resultado = grafico_medias_cm(df, "Tio Rafa")

        # Conferindo se ela não retorna nada com o erro
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = grafico_medias_cm()
        
        self.assertEqual(str(cm.exception), "grafico_medias_cm() missing 2 required positional arguments: 'df' and 'df_conc_medios'")

if __name__ == "__main__":
    unittest.main()