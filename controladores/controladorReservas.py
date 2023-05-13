from controladores.controladorSistema import ControladorSistema
from telas.telaSistema import TelaSistema
from telas.telaReservas import TelaReservas
from entidades.reserva import Reserva


class ControladorReservas:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__tela_reservas = TelaReservas()
        self.__controlador_sistema = controlador_sistema
        self.__reservas: list[Reserva] = []

    @property
    def reservas(self):
        return self.__reservas

    def incluir_reserva(self):
        dados_reserva = self.__tela_reservas.pega_dados_reserva()

        try:
            passageiro = self.pega_passageiro_por_cpf(dados_reserva["cpf_passageiro"])

            if not passageiro:
                # TODO usar exceções customizadas
                raise Exception("Passageiro não encontrado!")

            voo = self.pega_voo_por_codigo(dados_reserva["codigo_voo"])

            if not voo:
                # TODO usar exceções customizadas
                raise Exception("Voo não encontrado!")

            nova_reserva = Reserva(dados_reserva["assento"], passageiro, voo)
            self.reservas.append(nova_reserva)

            self.__tela_reservas.mostra_mensagem("Reserva realizada com sucesso!")

        except Exception as e:
            self.__tela_reservas.mostra_mensagem(str(e))

    def alterar_reserva(self):
        self.listar_reservas()
        codigo_reserva = self.__tela_reservas.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(codigo_reserva)

        if not reserva:
            self.__tela_reservas.mostra_mensagem("Reserva não encontrada!")

        else:
            dados_reserva = self.__tela_reservas.pega_dados_reserva()

            passageiro = None

            try:
                if dados_reserva["cpf_passageiro"]:
                    passageiro = self.pega_passageiro_por_cpf(
                        dados_reserva["cpf_passageiro"]
                    )

                    if not passageiro:
                        # TODO usar exceções customizadas
                        raise Exception("Passageiro não encontrado!")

                if dados_reserva["assento"]:
                    # TODO verificar se assento é válido
                    reserva.assento = dados_reserva["assento"]

                if passageiro:
                    reserva.passageiro = passageiro

            except Exception as e:
                self.__tela_reservas.mostra_mensagem(str(e))

    def excluir_reserva(self):
        self.listar_reservas()

        codigo_reserva = self.__tela_reservas.seleciona_reserva()
        reserva = self.pega_reserva_por_codigo(codigo_reserva)

        if not reserva:
            self.__tela_reservas.mostra_mensagem("Reserva não encontrada!")

        else:
            self.reservas.remove(reserva)
            self.__tela_reservas.mostra_mensagem("Reserva excluida com sucesso!")

    def listar_reservas(self):
        for reserva in self.reservas:
            self.__tela_reservas.mostra_reserva(
                {
                    "Codigo": reserva.codigo,
                    "Assento": reserva.assento,
                    # "Passageiro": reserva.passageiro.nome
                    # "Partida": reserva.voo.partida
                    # "Destino": reserva.voo.destino
                    # "Data": reserva.voo.data
                }
            )

    def pega_reserva_por_codigo(self, codigo: str):
        for reserva in self.reservas:
            if reserva.codigo == codigo:
                return reserva

        return None

    def pega_passageiro_por_cpf(self, cpf: str):
        pass
        # return (
        #     self.__controlador_sistema.controlador_passageiros.pega_passageiro_por_cpf(
        #         cpf
        #     )
        # )

    def pega_voo_por_codigo(self, codigo: str):
        pass
        # return self.__controlador_sistema.controlador_voos.pega_voo_por_codigo(codigo)

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
