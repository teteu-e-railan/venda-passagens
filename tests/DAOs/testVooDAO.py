import unittest
from datetime import datetime
from DAOs.voo_dao import VooDAO
from entidades.aviao import Aviao
from entidades.voo import Voo


class TestVooDAO(unittest.TestCase):
    def setUp(self):
        """Inicia o teste com valores pré setados."""
        self.__voo_dao = VooDAO()
        self.__aviao_teste = Aviao("1234", 6, 3)
        self.__voo_teste = Voo("teste", "teste", datetime.now(), self.__aviao_teste)

    def tearDown(self):
        """Limpa os dados armazenados ao terminar a execucao do teste."""
        self.__voo_dao.clear()

    def teste_add(self):
        """Testa a adição de um voo no arquivo de persistência."""
        self.__voo_dao.add(self.__voo_teste)

        self.assertTrue(
            self.__voo_dao.has(self.__voo_teste.codigo),
            "Não foi possível armazenar o voo!",
        )

    def teste_get_voo(self):
        """
        Testa a obtenção de um voo que esteja armazenado no arquivo de persistência.
        """
        self.__voo_dao.add(self.__voo_teste)

        voo = self.__voo_dao.get(self.__voo_teste.codigo)

        self.assertIsNotNone(
            voo,
            """
            Não foi possivel obter o voo, certifique-se que
            o código está certo ou que o voo esteja armazenado!
            """,
        )

    def teste_remove_voo(self):
        """Testa a remoção de um voo armazenado."""
        self.__voo_dao.add(self.__voo_teste)
        self.__voo_dao.remove(self.__voo_teste.codigo)

        self.assertFalse(
            self.__voo_dao.has(self.__voo_teste.codigo),
            "Não foi possível remover o voo!",
        )

    def teste_update_voo(self):
        """Testa a atualização de um voo armazenado."""
        self.__voo_dao.add(self.__voo_teste)

        self.__voo_teste.partida = "nova_partida"

        self.__voo_dao.update(self.__voo_teste)

        voo_modificado = self.__voo_dao.get(self.__voo_teste.codigo)

        self.assertEqual(
            voo_modificado.partida,
            "nova_partida",
            "Não foi possível atualizar o voo desejado!",
        )
