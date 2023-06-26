import unittest
from datetime import datetime
from DAOs.reserva_dao import ReservaDAO
from entidades.aviao import Aviao
from entidades.voo import Voo
from entidades.reserva import Reserva
from entidades.passageiro import Passageiro


class TestReservaDAO(unittest.TestCase):
    def setUp(self):
        """Inicia o teste com valores pré setados."""
        self.__reserva_dao = ReservaDAO()
        self.__aviao_teste = Aviao("1234", 6, 3)
        self.__passageiro_teste = Passageiro("teste", "12345", 30, 30)
        self.__voo_teste = Voo("teste", "teste", datetime.now(), self.__aviao_teste)
        self.__reserva_teste = Reserva(1, 1, self.__passageiro_teste, self.__voo_teste)

    def tearDown(self):
        """Limpa os dados armazenados ao terminar a execucao do teste."""
        self.__reserva_dao.clear()

    def teste_add_reserva(self):
        """Testa a adição de uma reserva no arquivo de persistência."""
        self.__reserva_dao.add(self.__reserva_teste)

        self.assertTrue(
            self.__reserva_dao.has(self.__reserva_teste.codigo),
            "Não foi possível armazenar a reserva!",
        )

    def teste_get_reserva(self):
        """
        Testa a obtenção de uma reserva que esteja
        armazenada no arquivo de persistência.
        """
        self.__reserva_dao.add(self.__reserva_teste)

        reserva = self.__reserva_dao.get(self.__reserva_teste.codigo)

        self.assertIsNotNone(
            reserva,
            """
            Não foi possivel obter a reserva, certifique-se que
            o código está certo ou que a reserva esteja armazenado!
            """,
        )

    def teste_remove_reserva(self):
        """Testa a remoção de uma reserva armazenada."""
        self.__reserva_dao.add(self.__reserva_teste)
        self.__reserva_dao.remove(self.__reserva_teste.codigo)

        self.assertFalse(
            self.__reserva_dao.has(self.__reserva_teste.codigo),
            "Não foi possível remover a reserva!",
        )

    def teste_update_reserva(self):
        """Testa a atualização de uma reserva armazenada."""
        self.__reserva_dao.add(self.__reserva_teste)

        self.__reserva_teste.passageiro = "novo_passageiro"

        self.__reserva_dao.update(self.__reserva_teste)

        reserva_modificada = self.__reserva_dao.get(self.__reserva_teste.codigo)

        self.assertEqual(
            reserva_modificada.passageiro,
            "novo_passageiro",
            "Não foi possível atualizar a reserva desejada!",
        )
