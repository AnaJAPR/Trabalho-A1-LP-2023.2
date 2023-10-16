import sys
sys.path.append('.') # assim o python procura os modulos a serem importados em todo o respositório atual. Importante para o import de analise_ana.py
import unittest
from analise_ana import cria_plot_1_ana, analise_1_ana, df 

class TestCriaPlot1Ana(unittest.TestCase):
    # teste com parâmetro válido
    def test_cria_plot_1_ana_com_dicionario(self):
        
        # Chama a função a ser testada
        resultado = cria_plot_1_ana(analise_1_ana(df))
        self.assertIsNone(resultado) 
    
    # teste com parâmetro inválido, ou seja, um que não seja dicionário
    def test_cria_plot_1_ana_sem_dicionario(self):
        
        resultado = cria_plot_1_ana("juju")
        # Verifica se a função retorna None neste caso
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_cria_plot_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = cria_plot_1_ana()
        
        self.assertEqual(str(cm.exception), "cria_plot_1_ana() missing 1 required positional argument: 'dicionario_contagem'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()