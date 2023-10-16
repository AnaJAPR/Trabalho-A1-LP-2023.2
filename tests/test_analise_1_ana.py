import sys
sys.path.append('.')
import unittest
import doctest
from analise_ana import analise_1_ana, df 

class TestAnalise1Ana(unittest.TestCase):
    def test_analise_1_ana_com_dataframe(self):
        # Chama a função de teste
        resultado = analise_1_ana(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, dict)
        self.assertEqual(len(resultado), 5)
    
    def test_analise_1_ana_sem_dataframe(self):
        # Chame a função com argumento inválido (não um DataFrame)
        resultado = analise_1_ana("Isso não é um DataFrame")

        # Verifique se a função retorna None neste caso
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()