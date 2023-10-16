import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
import doctest
from func_analises import reindexacao_e_filtragem, df 

class TestReindexacaoEFiltragem(unittest.TestCase):
    # teste com parâmetro válido
    def test_reindexacao_e_filtragem_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = reindexacao_e_filtragem(df, "Conceito Médio de Graduação")

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, pd.core.frame.DataFrame) # Resultado é um DataFrame pandas

    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_reindexacao_e_filtragem_com_coluna_errada(self):
        
        resultado = reindexacao_e_filtragem(df, "Tio Rafa")

        # Conferindo se ela não retorna nada com o erro
        self.assertIsNone(resultado)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = reindexacao_e_filtragem()
        
        self.assertEqual(str(cm.exception), "reindexacao_e_filtragem() missing 2 required positional arguments: 'df' and 'coluna'")

if __name__ == "__main__":
    unittest.main()