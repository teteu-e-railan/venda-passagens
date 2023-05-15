from entidades.passageiro import Passageiro
from telas.telaPassageiro import TelaPassagerio
from excepitions.passageiroJahExisteException import PassageiroJahExisteException


class ControladorPassageiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_passageiro = TelaPassagerio()
        self.__passageiros: list[Passageiro] = []

    def buscar_passageiro_por_cpf(self, cpf):
        for passageiro in self.__passageiros:
            if passageiro.cpf == cpf:
                return passageiro
        return None

    def incluir_passageiro(self):
        while True:
            dados_passageiro = self.__tela_passageiro.pega_dados_passageiro()
            if dados_passageiro is None:
                break

            try:
                for passageiro in self.__passageiros:
                    if passageiro.cpf == dados_passageiro["cpf"]:
                        raise PassageiroJahExisteException

                novo_passageiro = Passageiro(
                    dados_passageiro["nome"],
                    dados_passageiro["cpf"],
                    dados_passageiro["idade"],
                    dados_passageiro["telefone"],
                )
                self.__passageiros.append(novo_passageiro)
                self.__tela_passageiro.mostra_mensagem(
                    "Passageiro cadastrado com sucesso!!!"
                )

            except PassageiroJahExisteException:
                self.__tela_passageiro.mostra_mensagem(
                    "ATENÇÃO: passageiro já existe!!!"
                )
            if not self.__tela_passageiro.confirma_opcao(
                "Deseja cadastrar outro passageiro?"
            ):
                break

    def alterar_passageiro(self):
        self.listar_passageiros_nome_cpf()
        cpf = self.__tela_passageiro.seleciona_passageiro_por_cpf()
        passageiro = self.buscar_passageiro_por_cpf(cpf)

        if passageiro is None:
            self.__tela_passageiro.mostra_mensagem("Passageiro não encontrado!!!")

        else:
            self.__tela_passageiro.mostra_passageiro(
                {
                    "Nome": passageiro.nome,
                    "Cpf": passageiro.cpf,
                    "Idade": passageiro.idade,
                    "Telefone": passageiro.telefone,
                }
            )

            if self.__tela_passageiro.confirma_opcao(
                "Deseja realmente alterar este passageiro?"
            ):
                dados_passageiro = self.__tela_passageiro.altera_dados_passageiro()

                if dados_passageiro["nome"]:
                    passageiro.nome = dados_passageiro["nome"]

                if dados_passageiro["cpf"]:
                    passageiro.cpf = dados_passageiro["cpf"]

                if dados_passageiro["idade"]:
                    passageiro.idade = dados_passageiro["idade"]

                if dados_passageiro["telefone"]:
                    passageiro.telefone = dados_passageiro["telefone"]

                self.__tela_passageiro.mostra_mensagem(
                    "Passageiro alterado com sucesso!!!"
                )

            else:
                self.__tela_passageiro.mostra_mensagem(
                    "Alteração de passageiro cancelada!!!"
                )

    def listar_passageiros(self):
        if not self.__passageiros:
            self.__tela_passageiro.mostra_mensagem("Nenhum passageiro cadastrado!!!")
        else:
            for passageiro in self.__passageiros:
                self.__tela_passageiro.mostra_passageiro(
                    {
                        "Nome": passageiro.nome,
                        "CPF": passageiro.cpf,
                        "Idade": passageiro.idade,
                        "Telefone": passageiro.telefone,
                    }
                )

    def listar_passageiros_nome_cpf(self):
        for passageiro in self.__passageiros:
            self.__tela_passageiro.mostra_passageiro(
                {
                    "Passageiro": passageiro.nome,
                    "CPF": passageiro.cpf,
                }
            )

    def excluir_passageiro(self):
        while True:
            self.listar_passageiros_nome_cpf()
            cpf_passageiro = self.__tela_passageiro.seleciona_passageiro_por_cpf()
            passageiro = self.buscar_passageiro_por_cpf(cpf_passageiro)

            if passageiro is not None:
                if self.__tela_passageiro.confirma_opcao(
                    "Deseja realmente excluir este passageiro?"
                ):
                    self.__passageiros.remove(passageiro)
                    self.__tela_passageiro.mostra_mensagem(
                        "Passageiro excluído com sucesso!!!"
                    )
                else:
                    self.__tela_passageiro.mostra_mensagem(
                        "Exclusão de passageiro cancelada!!!"
                    )
                break

            else:
                opcao = self.__tela_passageiro.confirma_opcao(
                    "Passageiro não encontrado. Deseja buscar outro? "
                )
                if not opcao:
                    break

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_passageiro,
            2: self.alterar_passageiro,
            3: self.listar_passageiros,
            4: self.excluir_passageiro,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_passageiro.tela_opcoes()
            opcoes_controlador[opcao]()