import pandas as pd
import numpy as np
import sys
sys.path.append('.')
import unittest
from limpa_dados import remove_colunas_sem_dado, df 

class TestRemoveColunasSemDado(unittest.TestCase):
    # teste com parâmetro válido
    def test_remove_colunas_sem_dado_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = remove_colunas_sem_dado(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, pd.core.frame.DataFrame) # Resultado é um DataFrame pandas
        
    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_remove_colunas_sem_dado_sem_dataframe(self):
        
        resultado = remove_colunas_sem_dado("Tio Rafa")

        # O finally da função faz com que ela retorne o parametro pedido caso não seja um DataFrame
        self.assertIsInstance(resultado, str) 
        self.assertEqual(resultado, "Tio Rafa")
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = remove_colunas_sem_dado()
        
        self.assertEqual(str(cm.exception), "remove_colunas_sem_dado() missing 1 required positional argument: 'df'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()