import pandas as pd
import numpy as np
import sys
sys.path.append(".")
import unittest
import doctest
from func_analises import media_tres_por_indice, df 

class TestReindexacaoEFiltragem(unittest.TestCase):
    # teste com parâmetro válido
    def test_media_tres_por_indice_com_dataframe(self):
        
        # Chama a função a ser testada
        resultado = media_tres_por_indice(df, ["Conceito Médio de Graduação",
                                                "Conceito Médio de Mestrado", "Conceito Médio do doutorado"], "Categoria Administrativa")

        # Adiciona as asserções apropriadas para verificar o resultado
        self.assertIsInstance(resultado, pd.core.frame.DataFrame) # Resultado é um DataFrame pandas
    
    # teste sem parâmetro
    def test_analise_1_ana_sem_parametro(self):
        with self.assertRaises(TypeError) as cm:
            resultado = media_tres_por_indice()
        
        self.assertEqual(str(cm.exception), "media_tres_por_indice() missing 3 required positional arguments: 'df', 'lista_colunas', and 'indice'")

if __name__ == "__main__":
    unittest.main()