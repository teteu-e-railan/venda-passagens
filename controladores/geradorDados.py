from entidades.aviao import Aviao
from entidades.passageiro import Passageiro
from entidades.tripulante import Tripulante
from entidades.voo import Voo


class GerarDados:
    def __init__(
        self,
    ):
        self.listagem_gerada_aviao = [
            {"modelo": "BPTX320A", "fileiras": 18, "assentos_por_fileira": 4},
            {"modelo": "USTX420X", "fileiras": 28, "assentos_por_fileira": 4},
            {"modelo": "AIRBUS320", "fileiras": 36, "assentos_por_fileira": 6},
        ]
        self.listagem_gera_passageiros = [
            {
                "nome": "Railan Abreu",
                "cpf": 363636,
                "idade": 24,
                "telefone": 319955966,
            },
            {
                "nome": "Matheus Pissaia",
                "cpf": 365488,
                "idade": 22,
                "telefone": 999556677,
            },
            {
                "nome": "Pedro Carlos",
                "cpf": 886655,
                "idade": 12,
                "telefone": 999884411,
            },
        ]
        self.listagem_gera_tripulante = [
            {
                "nome": "Jorge e Matheus",
                "cpf": 686868,
                "idade": 36,
                "telefone": 319955966,
                "cargo": "Comisario de Bordo",
            },
            {
                "nome": "Matheus Pissaia",
                "cpf": 221722,
                "idade": 22,
                "telefone": 999556677,
                "cargo": "Piloto",
            },
            {
                "nome": "Ana Castela",
                "cpf": 886655,
                "idade": 12,
                "telefone": 999884411,
                "cargo": "Aeromoça",
            },
        ]
        self.listagem_gera_voo = [
            {
                "partida": "",
                "destino": 0,
                "data_do_voo": 0,
            },
            {
                "partida": "",
                "destino": 0,
                "data_do_voo": 0,
            },
            {
                "partida": "",
                "destino": 0,
                "data_do_voo": 0,
            },
        ]
