import sys
sys.path.append('.') # assim o python procura os modulos a serem importados em todo o respositório atual. Importante para o import de analise_ana.py
import unittest
from unittest.mock import Mock, patch
from analise_ana import cria_plot_2_ana, cria_plot_1_ana, analise_1_ana, analise_ana_2, df 

class TestCriaPlot2Ana(unittest.TestCase):
    # teste com parâmetro válido
    def test_cria_plot_2_ana_com_dicionario(self):
         # Cria um Mock para plt.show() para evitar que o gráfico seja exibido
        mock_show = Mock()
        with patch('matplotlib.pyplot.show', mock_show):
            # Chama a função a ser testada
            resultado = cria_plot_2_ana(analise_ana_2(analise_1_ana(df)))
            self.assertIsNone(resultado) 
    
    # teste com parâmetro inválido, ou seja, um que não seja dicionário
    def test_cria_plot_2_ana_sem_dicionario(self):
        
        self.assertIsNone(cria_plot_2_ana("juju"))
        self.assertIsNone(cria_plot_2_ana(6))
    
    # teste sem parâmetro
    def test_cria_plot_2_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = cria_plot_2_ana()
        
        self.assertEqual(str(cm.exception), "cria_plot_2_ana() missing 1 required positional argument: 'media_arredondada'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()