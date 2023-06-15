import string
from DAOs.reserva_dao import ReservaDAO
from telas.telaReservas import TelaReservas
from entidades.reserva import Reserva
from entidades.passageiro import Passageiro
from entidades.voo import Voo


class ControladorReservas:
    def __init__(self, controlador_sistema):
        self.__tela_reservas = TelaReservas()
        self.__controlador_sistema = controlador_sistema
        self.__reserva_dao = ReservaDAO()

    @property
    def reservas(self):
        return self.__reserva_dao.get_all()

    def incluir_reserva(self):
        self.__controlador_sistema.controlador_passageiros.listar_passageiros_nome_cpf()

        while True:
            cpf = self.__tela_reservas.pega_cpf()

            passageiro = self.pega_passageiro_por_cpf(cpf)

            if passageiro:
                break

            self.__tela_reservas.mostra_mensagem("Passageiro não encontrado!")

        self.__controlador_sistema.controlador_voos.listar_voos()

        while True:
            codigo_voo = self.__tela_reservas.pega_voo()

            voo = self.pega_voo_por_codigo(codigo_voo)

            if voo:
                break

            self.__tela_reservas.mostra_mensagem("Voo não encontrado!")

        self.__tela_reservas.mostra_assentos_voo(voo)

        while True:
            fileira = self.__tela_reservas.pega_fileira()

            if fileira <= voo.aviao.fileiras:
                break

            self.__tela_reservas.mostra_mensagem("Fileira inválida")

        while True:
            str_assento = self.__tela_reservas.pega_assento_fileira()
            assento_fileira = string.ascii_uppercase.index(str_assento)

            if assento_fileira <= voo.aviao.assentos_por_fileira - 1:
                break

            self.__tela_reservas.mostra_mensagem("Assento inválido!")

        try:
            nova_reserva = Reserva(fileira, assento_fileira, passageiro, voo)
            voo.reservar_assento(fileira - 1, assento_fileira)
            self.reservas.append(nova_reserva)

            self.__tela_reservas.mostra_mensagem("Reserva realizada com sucesso!")

        except Exception as e:
            self.__tela_reservas.mostra_mensagem(str(e))

    def alterar_reserva(self):
        self.listar_reservas()

        if not self.reservas:
            self.__tela_reservas.mostra_mensagem(
                "Não há nenhuma reserva registrada ainda :( "
            )

        codigo_reserva = self.__tela_reservas.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(codigo_reserva)

        if not reserva:
            self.__tela_reservas.mostra_mensagem("Reserva não encontrada!")

        else:
            try:
                self.__controlador_sistema.controlador_passageiros.listar_passageiros_nome_cpf()

                cpf = self.__tela_reservas.pega_cpf(alterando=True)

                if cpf:
                    passageiro = self.pega_passageiro_por_cpf(cpf)

                    if not passageiro:
                        # TODO usar exceções customizadas
                        raise Exception("Passageiro não encontrado!")

                self.__tela_reservas.mostra_assentos_voo(reserva.voo)

                fileira = self.__tela_reservas.pega_fileira(alterando=True)

                if fileira:
                    if fileira > reserva.voo.aviao.fileiras:
                        raise Exception("Fileira inválida")

                else:
                    fileira = reserva.fileira

                assento = self.__tela_reservas.pega_assento_fileira(alterando=True)

                if assento:
                    assento = string.ascii_uppercase.index(assento)

                    if assento > reserva.voo.aviao.assentos_por_fileira - 1:
                        raise Exception("Assento inválido")

                else:
                    assento = reserva.assento

                if reserva.voo.verifica_assento_ocupado(fileira - 1, assento):
                    raise Exception("O assento já encontra-se ocupado")

                reserva.voo.remover_assento_reservado(
                    reserva.fileira - 1, reserva.assento
                )

                reserva.fileira = fileira
                reserva.assento = assento
                reserva.voo.reservar_assento(fileira - 1, assento)

                self.__tela_reservas.mostra_mensagem("Reserva alterada com sucesso!")

            except Exception as e:
                self.__tela_reservas.mostra_mensagem(str(e))

    def excluir_reserva(self):
        self.listar_reservas()

        if not self.reservas:
            self.__tela_reservas.mostra_mensagem("Nenhuma reserva registrada ainda :( ")

        codigo_reserva = self.__tela_reservas.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(codigo_reserva)

        if not reserva:
            self.__tela_reservas.mostra_mensagem("Reserva não encontrada!")

        else:
            self.reservas.remove(reserva)
            self.__tela_reservas.mostra_mensagem("Reserva excluida com sucesso!")

    def listar_reservas(self):
        if not self.reservas:
            self.__tela_reservas.mostra_mensagem("Nenhuma reserva registrada ainda :( ")

        for reserva in self.reservas:
            self.__tela_reservas.mostra_reserva(
                {
                    "Codigo": reserva.codigo,
                    "Assento": f"{reserva.fileira}{string.ascii_uppercase[reserva.assento]}",
                    "Passageiro": reserva.passageiro.nome,
                    "Partida": reserva.voo.partida,
                    "Destino": reserva.voo.destino,
                    "Data": reserva.voo.data_do_voo.strftime("%d/%m/%Y"),
                }
            )

    def pega_reserva_por_codigo(self, codigo: str):
        for reserva in self.reservas:
            if reserva.codigo == codigo:
                return reserva

        return None

    def pega_passageiro_por_cpf(self, cpf: str) -> "Passageiro | None":
        return self.__controlador_sistema.controlador_passageiros.buscar_passageiro_por_cpf(
            cpf
        )

    def pega_voo_por_codigo(self, codigo: str) -> "Voo | None":
        return self.__controlador_sistema.controlador_voos.buscar_voo_por_codigo(codigo)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_reserva,
            2: self.alterar_reserva,
            3: self.excluir_reserva,
            4: self.listar_reservas,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_reservas.mostra_opcoes()

            opcoes_controlador[opcao_escolhida]()
