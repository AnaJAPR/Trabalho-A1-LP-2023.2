import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
from func_analises import df 
from analise_guilherme import prints_da_analise_das_medias

class TestReindexacaoEFiltragem(unittest.TestCase):
    # teste com parâmetro válido
    def test_prints_da_analise_das_medias_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = prints_da_analise_das_medias(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsNone(resultado) # A função não deve retornar nada

    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_prints_da_analise_das_medias_sem_receber_df(self):
        
        resultado = prints_da_analise_das_medias("Tio Rafa")

        # Conferindo se ela não retorna nada com o erro
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = prints_da_analise_das_medias()
        
        self.assertEqual(str(cm.exception), "prints_da_analise_das_medias() missing 1 required positional argument: 'df'")

if __name__ == "__main__":
    unittest.main()