import unittest
import doctest
from analise_ana import analise_1_ana

class TestAnalise1Ana(unittest.TestCase):
    def test_analise_1_ana(self):
        # Usa doctest.DocTestSuite para criar uma suíte de testes a partir do doctest
        doctest_suite = doctest.DocTestSuite(analise_1_ana)

        # Adiciona a suíte do doctest à suíte de testes do unittest
        self.addTests(doctest_suite)

if __name__ == "__main__":
    unittest.main()