import sys
sys.path.append('.') # assim o python procura os modulos a serem importados em todo o respositório atual. Importante para o import de analise_ana.py
import unittest
import doctest
from analise_ana import analise_1_ana, df 

class TestAnalise1Ana(unittest.TestCase):
    # teste com parâmetro válido
    def test_analise_1_ana_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = analise_1_ana(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, dict) # Resultado é instância de dicionário
        self.assertEqual(len(resultado), 5) # O resultado é composto por 5 itens
        for value in resultado.values(): 
            if not isinstance(value, dict):
                raise AssertionError("Esse valor não é um dicionário!") # Mensagem de erro esperada para o caso de um valor de resultado não ser um dicionário também
    
    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_analise_1_ana_sem_dataframe(self):
        
        resultado = analise_1_ana("Juju")

        # Verifica se a função retorna None neste caso
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = analise_1_ana()
        
        self.assertEqual(str(cm.exception), "analise_1_ana() missing 1 required positional argument: 'df'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()