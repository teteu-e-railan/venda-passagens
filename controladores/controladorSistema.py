from telas.telaSistema import TelaSistema
from controladores.controladorReservas import ControladorReservas


class ControladorSistema:
    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()
        self.__controlador_reservas = ControladorReservas(self)
        self.__controlador_passageiros = None
        self.__controlador_tripulantes = None
        self.__controlador_voos = None
        self.__controlador_avioes = None

    @property
    def controlador_reservas(self) -> ControladorReservas:
        return self.__controlador_reservas

    @property
    def controlador_passageiros(self):
        return self.__controlador_passageiros

    @property
    def controlador_tripulantes(self):
        return self.__controlador_tripulantes

    @property
    def controlador_voos(self):
        return self.__controlador_voos

    @property
    def controlador_avioes(self):
        return self.__controlador_avioes

    def inicializa_sistema(self):
        self.abre_tela()

    def finaliza_sistema(self):
        exit(0)

    def abre_tela(self):
        opcoes_controlador = {
            1: self.controlador_reservas.abre_tela,
            2: self.controlador_passageiros,
            3: self.controlador_tripulantes,
            4: self.controlador_voos,
            5: self.controlador_avioes,
            0: self.finaliza_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_opcoes()

            # TODO:
            # quando os controladores estiverem implementados,
            # usar `opcao_escolhida` para chamar o controlador desejado.
            opcoes_controlador[0]()
