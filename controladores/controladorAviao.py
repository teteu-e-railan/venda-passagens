from entidades.aviao import Aviao
from telas.telaAviao import TelaAviao
from excepitions.aviaoJahExisteException import AviaoJahExisteException


"""
INCLUIR OS .UPPER() EM TODOS OS IMPUTS QUE SÃO STR, TESTE 
NOS NOME DOS PASSAGEIROS DEVE SE INCLUIR
O .TITLE(), QUANDO FOR ALTERAR UM AVIAO DEVE SE MOSTRA OS DADOS
QUE FORAM ALTERADOS E UMA MENSGAEM DE SUCESSO!
FALTA INCLUIR UMA MENSAGEM DE QUANDO O AVIAO JA EXISTE DENTRO DA LISTA

"""


class ControladorAviao:
    def __init__(self, controlador_sistema=None):
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
                        raise AviaoJahExisteException
                novo_aviao = Aviao(
                    dados_aviao["modelo"],
                    dados_aviao["fileiras"],
                    dados_aviao["assentos_por_fileira"],
                )
                self.__avioes.append(novo_aviao)
            except Exception:
                pass

    def alterar_aviao(self):
        modelo = self.__tela_aviao.seleciona_aviao()
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
            self.__tela_aviao.mostra_aviao(
                {
                    "modelo": aviao.modelo,
                    "fileiras": aviao.fileiras,
                    "assentos_por_fileira": aviao.assentos_por_fileira,
                }
            )

    def excluir_aviao(self):
        self.listar_avioes()
        modelo_aviao = self.__tela_aviao.seleciona_aviao()
        aviao = self.buscar_aviao_por_modelo(modelo_aviao)

        if aviao is not None:
            self.__avioes.remove(aviao)
            self.listar_avioes()
        else:
            self.__tela_aviao.mostra_mensagem("ATENCAO: aviao não existente")
        # INCLUIR UMA MENSAGEM DE SUCESSO E O MODELO DE AVIÃO QUE FOI EXCLUIDO.

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_aviao,
            2: self.alterar_aviao,
            3: self.listar_avioes,
            4: self.excluir_aviao,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_aviao.tela_opcoes()
            opcoes_controlador[opcao]()
