import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
import doctest
from limpa_dados import trata_celulas_vazias, df 

class TestTrataCelulasVazias(unittest.TestCase):
    # teste com parâmetro válido
    def test_trata_celulas_vazias_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = trata_celulas_vazias(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, pd.core.frame.DataFrame) # Resultado é um DataFrame pandas
        
        # lista_nulos = list()
        # for coluna in resultado.columns.tolist():
        #     for indice in range(len(resultado)):
        #         celula = resultado[coluna].iloc[indice]
        #         if isinstance(celula, np.NaN):
        #             lista_nulos.append(resultado[coluna].iloc[indice])
        #         if len(lista_nulos) > resultado.shape[0] / 2:    
        #             raise AssertionError("Essa coluna nçao foi tratada!")
    
    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_trata_celulas_vazias_sem_dataframe(self):
        
        resultado = trata_celulas_vazias(42)

        # O finally da função faz com que ela retorne o parametro pedido caso não seja um DataFrame
        self.assertIsInstance(resultado, int) 
        self.assertEqual(resultado, 42)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm: # Espera-se que a função levante um erro
            resultado = trata_celulas_vazias()
        
        self.assertEqual(str(cm.exception), "trata_celulas_vazias() missing 1 required positional argument: 'df'") # Mensagem de erro esperada

if __name__ == "__main__":
    unittest.main()