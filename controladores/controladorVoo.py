from entidades.voo import Voo
from entidades.aviao import Aviao
from telas.telaVoo import TelaVoo
from entidades.registro import Registro
from DAOs.voo_dao import VooDAO
import datetime


class ControladorVoo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_voo = TelaVoo()
        self.__voo_dao = VooDAO()
        self.registros: list[Registro] = []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    @property
    def voos(self):
        return self.__voo_dao.get_all()

    def buscar_voo_por_codigo(self, codigo):
        for voo in self.voos:
            if voo.codigo == codigo:
                return voo

        return None

    def incluir_voo(self):
        dados_voo = self.__tela_voo.pega_dados_voo()
        aviao = self.pega_aviao_por_modelo(dados_voo["modelo_aviao"])

        try:
            if not aviao:
                # TODO usar excecoes customizadas
                raise Exception("Aviao nao encontrado!")

            for voo in self.voos:
                if (
                    voo.partida == dados_voo["partida"]
                    and voo.destino == dados_voo["destino"]
                    and voo.aviao == aviao.modelo
                ):
                    raise Exception("Esse Voo já existe!")

            novo_voo = Voo(
                dados_voo["partida"],
                dados_voo["destino"],
                dados_voo["data_do_voo"],
                aviao,
            )

            self.__voo_dao.add(novo_voo)

            # Registro automático no histórico
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            descricao = f"Inclusão de avião: {novo_voo.codigo, novo_voo.destino}"
            registro = Registro(data, descricao)
            self.adicionar_registro(registro)

            self.__tela_voo.mostra_mensagem("Voo cadastrado com sucesso!")

        except Exception as e:
            self.__tela_voo.mostra_mensagem(str(e))
            return

    def alterar_voo(self):
        self.listar_voos()

        if not self.voos:
            return

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

            # Registro automático no histórico
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            descricao = f"Alyteração do voo: {dados_voo}"
            registro = Registro(data, descricao)
            self.adicionar_registro(registro)

            self.__voo_dao.update(voo)
            self.__tela_voo.mostra_mensagem("Voo alterado com sucesso!")

    def listar_voos(self):
        if not self.voos:
            self.__tela_voo.mostra_mensagem("Nenhum Voo cadastrado!")

        for voo in self.voos:
            self.__tela_voo.mostra_voo(
                {
                    "Codigo": voo.codigo,
                    "Partida": voo.partida,
                    "Destino": voo.destino,
                    "Data": voo.data_do_voo.strftime("%d/%m/%Y"),
                    "Modelo do Avião": voo.aviao.modelo,
                }
            )

    def excluir_voo(self):
        self.listar_voos()

        if not self.voos:
            return

        codigo_voo = self.__tela_voo.seleciona_voo()
        voo = self.buscar_voo_por_codigo(codigo_voo)

        if voo:
            self.__voo_dao.remove(voo.codigo)

            # Registro automático no histórico
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            descricao = f"Exclusão do voo: {voo}"
            registro = Registro(data, descricao)
            self.adicionar_registro(registro)

            self.__tela_voo.mostra_mensagem("Voo excluído com sucesso!")

        else:
            self.__tela_voo.mostra_mensagem("ATENCAO: Voo não encontrado!")

    def pega_aviao_por_modelo(self, modelo: "str | None") -> "Aviao | None":
        if modelo:
            return (
                self.__controlador_sistema.controlador_avioes.buscar_aviao_por_modelo(
                    modelo
                )
            )

    def listar_registros(self):
        if not self.registros:
            self.__tela_voo.mostra_mensagem("Nenhum Registro encontrado!!!")
        else:
            for registro in self.registros:
                self.__tela_voo.mostra_registro(
                    {
                        "Descrição": registro.descricao,
                        "Data e Hora": registro.data,
                    }
                )

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_voo,
            2: self.alterar_voo,
            3: self.listar_voos,
            4: self.excluir_voo,
            5: self.listar_registros,
            0: self.retornar,
        }

        while True:
            opcao = self.__tela_voo.tela_opcoes()
            opcoes_controlador[opcao]()
