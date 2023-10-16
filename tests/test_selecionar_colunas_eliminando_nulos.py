import sys
sys.path.append('.')
import unittest
from func_analises import selecionar_colunas_eliminando_nulos, df
import pandas as pd

class SelecionarColunasEliminandoNulos(unittest.TestCase):
    def teste_com_df_e_colunas(self):
        resultado = selecionar_colunas_eliminando_nulos(df, ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
    # Testa se o retorno da função é um DataFrame.
        self.assertIsInstance(resultado, pd.core.frame.DataFrame)

    def teste_sem_df_existente(self):
        resultado = selecionar_colunas_eliminando_nulos("Não sou um df", ["Beta (Proporção de Mestrado - Equivalente)", "Conceito Médio de Mestrado"])
    # Testa se o retorno da função é um DataFrame e se este é igual ao passado na função.
        self.assertNotIsInstance(resultado, pd.core.frame.DataFrame)
        self.assertTrue(resultado == "Não sou um df")

    def teste_colunas_nao_e_uma_lista(self):
        resultado = selecionar_colunas_eliminando_nulos(df, 4)
    # Testa se o retorno da função é um dataframe e se este é o mesmo passado inicialmente
        self.assertIsInstance(resultado, pd.core.frame.DataFrame)
        self.assertTrue(resultado.equals(df))

    def teste_coluna_nao_esta_no_df(self):
        resultado = selecionar_colunas_eliminando_nulos(df, ["a", "b", "c"])
    # Testa se o retorno da função é um dataframe e se este é o mesmo passado inicialmente
        self.assertIsInstance(resultado, pd.core.frame.DataFrame)
        self.assertTrue(resultado.equals(df))

if __name__ == "__main__":
    unittest.main()