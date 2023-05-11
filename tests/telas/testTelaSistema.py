import unittest
from telas.telaSistema import TelaSistema


class TestTelaSistema(unittest.TestCase):
    def teste_opcoes_tela_sistema(self):
        """Testa se as opcoes da Tela do Sistema sao as esperadas."""
        opcoes = {
            1: "Reservas",
            2: "Passageiros",
            3: "Tripulantes",
            4: "Voos",
            5: "Aviões",
            0: "Finalizar Sistema",
        }

        tela_sistema = TelaSistema()

        self.assertDictEqual(
            tela_sistema.opcoes,
            opcoes,
            "As opcoes da tela do sistema nao sao as esperadas!",
        )
