import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
from limpa_dados import corrige_nomes_df, df 

class TestCorrigeNomesDf(unittest.TestCase):
    # teste com parâmetro válido
    def test_corrige_nomes_df_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = corrige_nomes_df(df)

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, pd.core.frame.DataFrame) # Resultado é um DataFrame pandas
        
        for coluna_tratada in sorted(resultado.columns.tolist()):
            for coluna in sorted(df.columns.tolist()):
                if coluna[-1] == "*":
                    coluna = coluna.replace("*", "")
                    
                    if coluna[0] == " ":
                        self.assertEqual(coluna_tratada, coluna[1:])
                    else:
                        self.assertEqual(coluna_tratada, coluna)
    
    # teste com parâmetro inválido, ou seja, um que não seja DataFrame
    def test_corrige_nomes_df_sem_dataframe(self):
        
        resultado = corrige_nomes_df(42)

        # O finally da função faz com que ela retorne o parametro pedido caso não seja um DataFrame
        self.assertIsInstance(resultado, int) 
        self.assertEqual(resultado, 42)
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = corrige_nomes_df()
        
        self.assertEqual(str(cm.exception), "corrige_nomes_df() missing 1 required positional argument: 'df'")

if __name__ == "__main__":
    unittest.main()