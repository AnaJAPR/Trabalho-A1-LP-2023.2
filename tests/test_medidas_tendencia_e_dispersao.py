import sys
sys.path.append('.')
import unittest
from func_analises import medidas_tendencia_e_dispersao, df

class MedidasTendenciaEDispersao(unittest.TestCase):
    def teste_medidas_tendencia_e_dispersao_com_df_e_coluna(self):
        resultado = medidas_tendencia_e_dispersao(df, "Conceito Médio do doutorado")
    # Testa se o retorno da função é um dicionário contendo as 5 chaves (média, mediana, desvio padrão, máximo e mínimo)
        self.assertIsInstance(resultado, dict)
        self.assertEqual(len(resultado), 5)

    def testes_medidas_tendencia_e_dispersao_sem_df(self):
        resultado = medidas_tendencia_e_dispersao("Não sou um df", "Conceito Médio do doutorado")
    # Caso os argumentos não satisfaçam a função, ela não possui um retorno é vazio
        self.assertIsNone(resultado)

    def testes_medidas_tendencia_e_dispersao_sem_coluna(self):
        resultado = medidas_tendencia_e_dispersao(df, "Coluna Inexistente")
    # Caso os argumentos não satisfaçam a função, ela não possui um retorno é vazio
        self.assertIsNone(resultado)

    def testes_medidas_tendencia_e_dispersao_coluna_nao_numerica(self):
        resultado = medidas_tendencia_e_dispersao(df, "Sigla da UF")
    # Caso os argumentos não satisfaçam a função, ela não possui um retorno é vazio
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()