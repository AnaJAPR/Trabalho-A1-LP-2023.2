import sys
sys.path.append('.')
import unittest
from func_analises import medidas_tendencia_e_dispersao, df

class MedidasTendenciaEDispersao(unittest.TestCase):
    def teste_medidas_tendencia_e_dispersao_com_df_e_coluna(self):
        resultado = medidas_tendencia_e_dispersao(df, "Conceito Médio do doutorado")

        self.assertIsInstance(resultado, dict)
        self.assertEqual(len(resultado), 5)

    def testes_medidas_tendencia_e_dispersao_sem_df(self):
        resultado = medidas_tendencia_e_dispersao("Não sou um df", "Conceito Médio do doutorado")
        self.assertIsNone(resultado)

    def testes_medidas_tendencia_e_dispersao_sem_coluna(self):
        resultado = medidas_tendencia_e_dispersao(df, "Coluna Inexistente")
        self.assertIsNone(resultado)

    def testes_medidas_tendencia_e_dispersao_coluna_nao_numerica(self):
        resultado = medidas_tendencia_e_dispersao(df, "Sigla da UF")
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()