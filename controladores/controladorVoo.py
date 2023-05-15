from entidades.voo import Voo
from telas.telaVoo import TelaVoo
from controladores.controladorSistema import ControladorSistema


class ControladorVoo:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_voo = TelaVoo()
        self.__voos: list[Voo] = []

    @property
    def voos(self):
        return self.__voos

    def buscar_voo_por_codigo(self, codigo):
        for voo in self.voos:
            if voo.codigo == codigo:
                return voo

        return None

    def incluir_voo(self):
        dados_voo = self.__tela_voo.pega_dados_voo()
        aviao = self.pega_aviao_por_modelo(dados_voo["modelo_aviao"])

        if not aviao:
            # TODO usar excecoes customizadas
            raise Exception("Aviao nao encontrado")

        try:
            for voo in self.voos:
                if (
                    voo.partida == dados_voo["partida"]
                    and voo.destino == dados_voo["destino"]
                    and voo.aviao == aviao.modelo
                ):
                    raise Exception("Esse Voo já existe!")

        except Exception as e:
            self.__tela_voo.mostra_mensagem(str(e))

        novo_voo = Voo(
            dados_voo["partida"],
            dados_voo["destino"],
            dados_voo["data_do_voo"],
            aviao,
        )

        self.voos.append(novo_voo)
        self.__tela_voo.mostra_mensagem("Voo cadastrado com sucesso!")

    def alterar_voo(self):
        codigo_voo = self.__tela_voo.seleciona_voo()
        voo = self.buscar_voo_por_codigo(codigo_voo)

        if not voo:
            self.__tela_voo.mostra_mensagem("Voo não encontrado!")

        else:
            dados_voo = self.__tela_voo.pega_dados_altera_voo()

            if dados_voo["partida"]:
                voo.partida = dados_voo["partida"]

            if dados_voo["destino"]:
                voo.destino = dados_voo["destino"]

            if dados_voo["data_do_voo"]:
                voo.data_do_voo = dados_voo["data_do_voo"]

            self.__tela_voo.mostra_mensagem("Voo alterado com sucesso!")

    def listar_voos(self):
        for voo in self.voos:
            self.__tela_voo.mostra_voo(
                {
                    "Codigo": voo.codigo,
                    "Partida": voo.partida,
                    "Destino": voo.destino,
                    "Data": voo.data_do_voo,
                    "Aviao": voo.aviao.modelo,
                }
            )

    def excluir_voo(self):
        self.listar_voos()
        codigo_voo = self.__tela_voo.seleciona_voo()
        voo = self.buscar_voo_por_codigo(codigo_voo)

        if voo:
            self.voos.remove(voo)
            self.__tela_voo.mostra_mensagem("Voo excluído com sucesso!")
        else:
            self.__tela_voo.mostra_mensagem("ATENCAO: Voo não encontrado")

    def pega_aviao_por_modelo(self, modelo: "str | None"):
        if modelo:
            return (
                self.__controlador_sistema.controlador_avioes.buscar_aviao_por_modelo(
                    modelo
                )
            )

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_voo,
            2: self.alterar_voo,
            3: self.listar_voos,
            4: self.excluir_voo,
            0: self.retornar,
        }

        while True:
            opcao = self.__tela_voo.tela_opcoes()
            opcoes_controlador[opcao]()
