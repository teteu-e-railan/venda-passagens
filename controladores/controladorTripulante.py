from entidades.tripulante import Tripulante
from telas.telaTripulante import TelaTripulante
from excepitions.tripulanteJahExisteException import TripulanteJahExisteException


class ControladorTripulante:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tripulante = TelaTripulante()
        self.__tripulantes: list[Tripulante] = []

    def buscar_tripulante_por_cpf(self, cpf):
        for tripulante in self.__tripulantes:
            if tripulante.cpf == cpf:
                return tripulante
        return None

    def incluir_tripulante(self):
        while True:
            dados_tripulante = self.__tela_tripulante.pega_dados_tripulante()
            if dados_tripulante is None:
                break

            try:
                for tripulante in self.__tripulantes:
                    if tripulante.cpf == dados_tripulante["cpf"]:
                        raise TripulanteJahExisteException

                novo_tripulante = Tripulante(
                    dados_tripulante["nome"],
                    dados_tripulante["cpf"],
                    dados_tripulante["idade"],
                    dados_tripulante["telefone"],
                    dados_tripulante["cargo"],
                )
                self.__tripulantes.append(novo_tripulante)
                self.__tela_tripulante.mostra_mensagem(
                    "Tripulante cadastrado com sucesso!!!"
                )

            except TripulanteJahExisteException:
                self.__tela_tripulante.mostra_mensagem(
                    "ATENÇÃO: Tripulante já existe!!!"
                )
            if not self.__tela_tripulante.confirma_opcao(
                "Deseja cadastrar outro tripulante?"
            ):
                break

    def alterar_tripulante(self):
        self.listar_tripulantes_nome_cpf_cargo()
        cpf = self.__tela_tripulante.seleciona_tripulante_por_cpf()
        tripulante = self.buscar_tripulante_por_cpf(cpf)

        if tripulante is None:
            self.__tela_tripulante.mostra_mensagem("tripulante não encontrado!!!")

        else:
            self.__tela_tripulante.mostra_tripulante(
                {
                    "Nome": tripulante.nome,
                    "Cpf": tripulante.cpf,
                    "Idade": tripulante.idade,
                    "Telefone": tripulante.telefone,
                    "Cargo": tripulante.cargo,
                }
            )

            if self.__tela_tripulante.confirma_opcao(
                "Deseja realmente alterar este tripulante?"
            ):
                dados_tripulante = self.__tela_tripulante.altera_dados_tripulante()

                if dados_tripulante["nome"]:
                    tripulante.nome = dados_tripulante["nome"]

                if dados_tripulante["cpf"]:
                    tripulante.cpf = dados_tripulante["cpf"]

                if dados_tripulante["idade"]:
                    tripulante.idade = dados_tripulante["idade"]

                if dados_tripulante["telefone"]:
                    tripulante.telefone = dados_tripulante["telefone"]

                if dados_tripulante["cargo"]:
                    tripulante.cargo = dados_tripulante["cargo"]

                self.__tela_tripulante.mostra_mensagem(
                    "tripulante alterado com sucesso!!!"
                )

            else:
                self.__tela_tripulante.mostra_mensagem(
                    "Alteração de tripulante cancelada!!!"
                )

    def listar_tripulantes(self):
        if not self.__tripulantes:
            self.__tela_tripulante.mostra_mensagem("Nenhum tripulante cadastrado!!!")
        else:
            for tripulante in self.__tripulantes:
                self.__tela_tripulante.mostra_tripulante(
                    {
                        "Nome": tripulante.nome,
                        "CPF": tripulante.cpf,
                        "Idade": tripulante.idade,
                        "Telefone": tripulante.telefone,
                        "Cargo": tripulante.cargo,
                    }
                )

    def listar_tripulantes_nome_cpf_cargo(self):
        for tripulante in self.__tripulantes:
            self.__tela_tripulante.mostra_tripulante(
                {
                    "tripulante": tripulante.nome,
                    "CPF": tripulante.cpf,
                    "cargo": tripulante.cargo,
                }
            )

    def excluir_tripulante(self):
        while True:
            self.listar_tripulantes_nome_cpf_cargo()
            cpf_tripulante = self.__tela_tripulante.seleciona_tripulante_por_cpf()
            tripulante = self.buscar_tripulante_por_cpf(cpf_tripulante)

            if tripulante is not None:
                if self.__tela_tripulante.confirma_opcao(
                    "Deseja realmente excluir este tripulante?"
                ):
                    self.__tripulantes.remove(tripulante)
                    self.__tela_tripulante.mostra_mensagem(
                        "tripulante excluído com sucesso!!!"
                    )
                else:
                    self.__tela_tripulante.mostra_mensagem(
                        "Exclusão de tripulante cancelada!!!"
                    )
                break

            else:
                opcao = self.__tela_tripulante.confirma_opcao(
                    "tripulante não encontrado. Deseja buscar outro? "
                )
                if not opcao:
                    break

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes_controlador = {
            1: self.incluir_tripulante,
            2: self.alterar_tripulante,
            3: self.listar_tripulantes,
            4: self.excluir_tripulante,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_tripulante.tela_opcoes()
            opcoes_controlador[opcao]()
