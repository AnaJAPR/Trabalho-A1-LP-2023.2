import sys
sys.path.append('.') # assim o python procura os modulos a serem importados em todo o respositório atual. Importante para o import de analise_ana.py
import unittest
from analise_ana import analise_ana_2, analise_1_ana, df 

class TestAnaliseAna2(unittest.TestCase):
    # teste com parâmetro válido
    def test_analise_ana_2_com_dicionario(self):
        
        # Chama a função a ser testada
        resultado = analise_ana_2(analise_1_ana(df))

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, dict) # Resultado é instância de dicionário
        self.assertEqual(len(resultado), 5) # O resultado é composto por 5 itens
        
        # Verifica se os valores têm até 3 casas decimais
        for valor in resultado.values():
            self.assertTrue(isinstance(valor, (int, float)))  # Verifica se é um número
            casas_decimais = len(str(valor).split('.')[1]) if isinstance(valor, float) else 0 #verifica se é float e, assim, quantas casas decimais possui
            self.assertLessEqual(casas_decimais, 3)  # Verifica se tem até 3 casas decimais
    
    # teste com parâmetro inválido, ou seja, um que não seja dicionário
    def test_analise_ana_2_sem_dicionario(self):
        
        resultado = analise_ana_2("juju")
        
        # Verifica se a função retorna None neste caso
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_ana_2_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = analise_ana_2()
        
        self.assertEqual(str(cm.exception), "analise_ana_2() missing 1 required positional argument: 'dicionario_contagem'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()