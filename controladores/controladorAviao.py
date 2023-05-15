from entidades.aviao import Aviao
from telas.telaAviao import TelaAviao
from excepitions.aviaoJahExisteException import AviaoJahExisteException
from entidades.registro import Registro
import datetime


class ControladorAviao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aviao = TelaAviao()
        self.__avioes: list[Aviao] = []
        self.registros: list[Registro] = []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def buscar_aviao_por_modelo(self, modelo):
        for aviao in self.__avioes:
            if aviao.modelo == modelo:
                return aviao
        return None

    def incluir_aviao(self):
        while True:
            dados_aviao = self.__tela_aviao.pega_dados_aviao()
            if dados_aviao is None:
                break
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

                # Registro automático no histórico
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                descricao = f"Inclusão de avião: {novo_aviao.modelo}"
                registro = Registro(data, descricao)
                self.adicionar_registro(registro)

                self.__tela_aviao.mostra_mensagem("Avião cadastrado com sucesso!!!")
            except AviaoJahExisteException:
                self.__tela_aviao.mostra_mensagem("ATENÇÃO: Avião já existe!!!")
            if not self.__tela_aviao.confirma_opcao("Deseja cadastrar outro avião?"):
                break

    def alterar_aviao(self):
        self.listar_avioes()
        if not self.__avioes:
            return

        modelo = self.__tela_aviao.seleciona_aviao()
        aviao = self.buscar_aviao_por_modelo(modelo)

        if aviao is None:
            self.__tela_aviao.mostra_mensagem("aviao não encontrado!!!")

        else:
            self.__tela_aviao.mostra_aviao(
                {
                    "Modelo": aviao.modelo,
                    "Capacidade": aviao.assentos_total,
                }
            )

            if self.__tela_aviao.confirma_opcao("Deseja realmente alterar este aviao?"):
                dados_aviao = self.__tela_aviao.altera_dados_aviao()

                if dados_aviao["modelo"]:
                    aviao.modelo = dados_aviao["modelo"]

                if dados_aviao["fileiras"]:
                    aviao.fileiras = dados_aviao["fileiras"]

                if dados_aviao["assentos_por_fileira"]:
                    aviao.assentos_por_fileira = dados_aviao["assentos_por_fileira"]

                # Registro automático no histórico
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                descricao = f"Alteração de avião: {aviao.modelo}"
                registro = Registro(data, descricao)
                self.adicionar_registro(registro)

                self.__tela_aviao.mostra_mensagem("aviao alterado com sucesso!!!")

            else:
                self.__tela_aviao.mostra_mensagem("Alteração de aviao cancelada!!!")

    def listar_avioes(self):
        if not self.__avioes:
            self.__tela_aviao.mostra_mensagem("Nenhum avião cadastrado!!!")
        else:
            for aviao in self.__avioes:
                self.__tela_aviao.mostra_aviao(
                    {
                        "Modelo": aviao.modelo,
                        "Assentos total": aviao.assentos_total,
                    }
                )

    def excluir_aviao(self):
        while True:
            self.__tela_aviao.mostra_modelo(self.__avioes)
            modelo_aviao = self.__tela_aviao.seleciona_aviao()
            aviao = self.buscar_aviao_por_modelo(modelo_aviao)

            if aviao is not None:
                if self.__tela_aviao.confirma_opcao(
                    "Deseja realmente excluir este avião?"
                ):
                    self.__avioes.remove(aviao)

                    # Registro automático no histórico
                    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    descricao = f"Exclusão de avião: {aviao.modelo}"
                    registro = Registro(data, descricao)
                    self.adicionar_registro(registro)

                    self.__tela_aviao.mostra_mensagem(
                        f"Avião {modelo_aviao} excluído com sucesso!!!"
                    )
                else:
                    self.__tela_aviao.mostra_mensagem("Exclusão de avião cancelada!!!")
                break
            else:
                opcao = self.__tela_aviao.confirma_opcao(
                    "Modelo não encontrado. Deseja buscar outro modelo? "
                )
                if not opcao:
                    break

    def listar_registros(self):
        if not self.registros:
            self.__tela_aviao.mostra_mensagem("Nenhum Registro encontrado!!!")
        else:
            for registro in self.registros:
                self.__tela_aviao.mostra_registro(
                    {
                        "Descrição": registro.descricao,
                        "Data e Hora": registro.data,
                    }
                )

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_aviao,
            2: self.alterar_aviao,
            3: self.listar_avioes,
            4: self.excluir_aviao,
            5: self.listar_registros,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_aviao.tela_opcoes()
            opcoes_controlador[opcao]()
