from entidades.aviao import Aviao
from telas.telaAviao import TelaAviao


class ControladorAviao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aviao = TelaAviao()
        self.__avioes: list[Aviao] = []

    def buscar_aviao_por_modelo(self, modelo):
        for aviao in self.__avioes:
            if aviao.modelo == modelo:
                return aviao
        return None

    def incluir_aviao(self):
        dados_aviao = self.__tela_aviao.pega_dados_aviao()
        if dados_aviao is not None:
            try:
                for aviao in self.__avioes:
                    if aviao.modelo == dados_aviao["modelo"]:
                        raise Exception
                novo_aviao = Aviao(
                    dados_aviao["modelo"],
                    dados_aviao["fileiras"],
                    dados_aviao["assentos_por_fileira"],
                )
                self.__avioes.append(novo_aviao)
            except Exception:
                pass

    def alterar_aviao(self, modelo):
        aviao = self.buscar_aviao_por_modelo(modelo)
        if aviao is None:
            self.__tela_aviao.mostra_mensagem("Avião não encontrado!!!")
        else:
            dados_aviao = self.__tela_aviao.pega_dados_aviao()
            aviao.modelo = dados_aviao["modelo"]
            aviao.fileiras = dados_aviao["fileiras"]
            aviao.assentos_por_fileira = dados_aviao["assentos_por_fileira"]

    def listar_avioes(self):
        for aviao in self.__avioes:
            self.__tela_aviao.mostra_mensagem(
                {
                    "Modelo": aviao.modelo,
                    "Capacidade": aviao.__assentos_total,
                    "Fileiras": aviao.fileiras,
                    "Assentos por fileira": aviao.assentos_por_fileira,
                }
            )

    def excluir_aviao(self):
        self.listar_avioes()
        modelo_aviao = self.__tela_aviao.seleciona_aviao()
        aviao = self.buscar_aviao_por_modelo(modelo_aviao)

        if aviao is not None:
            self.__aviaos.remove(aviao)
            self.listar_avioes()
        else:
            self.__tela_aviao.mostra_mensagem("ATENCAO: aviao não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        self.__tela_aviao.tela_opcoes = {
            1: self.incluir_amigo,
            2: self.alterar_amigo,
            3: self.lista_amigos,
            4: self.excluir_amigo,
            0: self.retornar,
        }
