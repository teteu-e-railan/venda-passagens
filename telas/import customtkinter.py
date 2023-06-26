import customtkinter 

class TelaAviao:
    def mostra_registro(self, dados_aviao):
        # Configurações da interface gráfica
        customT.set_appearance_mode('dark')
        customT.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customT.CTk()
        nova_janela.geometry('500x600')
        nova_janela.title("Registro de Ações")

        frame = customT.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label_titulo = customT.CTkLabel(master=frame, text="Registro de Ações", font=('Tahoma', 20))
        label_titulo.pack(pady=12, padx=10)

        if not dados_aviao:
            label_mensagem = customT.CTkLabel(master=frame, text="Sem registros encontrados", font=('Tahoma', 12))
            label_mensagem.pack(pady=5)
        else:
            for index, valor in dados_aviao.items():
                label_dados = customT.CTkLabel(master=frame, text=f"{index}: {valor}", font=('Tahoma', 12))
                label_dados.pack(pady=5)

        def voltar():
            nova_janela.destroy()

        button_voltar = customT.CTkButton(master=frame, text="Voltar", command=voltar, width=10)
        button_voltar.pack(pady=10)

        nova_janela.mainloop()

import customtkinter as customT

class TelaPassageiro:
    def mostra_passageiro(self, dados_passageiro):
        # Configurações da interface gráfica
        customT.set_appearance_mode('dark')
        customT.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customT.CTk()
        nova_janela.geometry('400x300')
        nova_janela.title("Passageiro")

        # Criar o frame principal
        frame_principal = customT.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=40)

        # Verificar se há registros para exibir
        if not dados_passageiro:
            label_mensagem = customT.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
            label_mensagem.pack(pady=50)
        else:
            # Exibir os registros
            for index, valor in dados_passageiro.items():
                label_registro = customT.CTkLabel(master=frame_principal, text=f"{index}: {valor}", font=('Tahoma', 12))
                label_registro.pack()

        # Botão "Voltar"
        def voltar():
            nova_janela.destroy()

        botao_voltar = customT.CTkButton(master=frame_principal, text="Voltar", command=voltar)
        botao_voltar.pack(pady=10)

        nova_janela.mainloop()


import customtkinter as customT

class TelaPassageiro:
    def seleciona_passageiro_por_cpf(self):
        # Configurações da interface gráfica
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = ctk.CTk()
        nova_janela.geometry('400x200')
        nova_janela.title("Selecionar Passageiro por CPF")

        # Criar o frame principal
        frame_principal = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame_principal.pack(pady=20, padx=40)

        # Label e Entry para o CPF
        label_cpf = ctk.CTkLabel(master=frame_principal, text="CPF do passageiro:", font=('Tahoma', 12))
        label_cpf.pack()

        entry_cpf = ctk.CTkEntry(master=frame_principal, width=200)
        entry_cpf.pack(pady=5)

        # Botão "Selecionar"
        def selecionar():
            cpf = entry_cpf.get().strip()
            nova_janela.destroy()
            self.processa_passageiro_por_cpf(cpf)

        botao_selecionar = ctk.CTkButton(master=frame_principal, text="Selecionar", command=selecionar, width=10)
        botao_selecionar.pack(pady=10)

        nova_janela.mainloop()

    def processa_passageiro_por_cpf(self, cpf):
        # Lógica para processar o CPF do passageiro selecionado
        print(f"CPF selecionado: {cpf}")

import tkinter as tk
from tkinter import Scrollbar, Listbox

def mostra_passageiro(self, dados_passageiro):
    # Configurações da interface gráfica
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    # Criar uma nova janela
    nova_janela = tk.Tk()
    nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
    nova_janela.title("Passageiro")

    # Criar o frame principal
    frame_principal = tk.Frame(master=nova_janela, bg='green')
    frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

    # Criar o scrollbar
    scrollbar = Scrollbar(master=frame_principal)
    scrollbar.pack(side='right', fill='y')

    # Criar o listbox para exibir os registros
    listbox_passageiros = Listbox(master=frame_principal, font=('Tahoma', 14), bg='white', yscrollcommand=scrollbar.set)
    listbox_passageiros.pack(pady=1, padx=10, side='left', fill="both", expand=True)

    # Configurar o scrollbar para controlar o listbox
    scrollbar.config(command=listbox_passageiros.yview)

    # Verificar se há registros para exibir
    if not dados_passageiro:
        listbox_passageiros.insert("end", "Sem registros encontrados")
    else:
        listbox_passageiros.insert("end", "Passageiros cadastrados")

        # Exibir os registros
        for chave, valor in dados_passageiro.items():
            passageiro_texto = f"{chave}: {valor}"
            listbox_passageiros.insert("end", passageiro_texto)

    nova_janela.mainloop()

import customtkinter as ctk

def mostra_registro(self, dados_aviao):
    # Configurações da interface gráfica
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    # Criar uma nova janela
    nova_janela = ctk.CTk()
    nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
    nova_janela.title("Registros")

    # Criar o frame principal
    frame_principal = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='blue')
    frame_principal.pack(pady=20, padx=60, fill='both', expand=True)

    # Verificar se há registros para exibir
    if not dados_aviao:
        label_mensagem = ctk.CTkLabel(master=frame_principal, text="Sem registros encontrados", font=('Tahoma', 14))
        label_mensagem.pack(pady=50, padx=10, side='top', fill="both", expand=True)
    else:
        label_titulo = ctk.CTkLabel(master=frame_principal, text="Registros de Avião", font=('Tahoma', 20))
        label_titulo.pack(pady=12, padx=10, side='top', fill="both", expand=True)

        # Criar um frame para os registros
        frame_registros = ctk.CTkFrame(master=frame_principal)
        frame_registros.pack(pady=10, padx=10, side='top', fill="both", expand=True)

        # Exibir os registros
        for index, valor in dados_aviao.items():
            registro_str = f"{index}: {valor}"
            label_registro = ctk.CTkLabel(master=frame_registros, text=registro_str, font=('Tahoma', 14))
            label_registro.pack(pady=5, padx=10, side='top', fill="both", expand=True)

    nova_janela.mainloop()


def pega_dados_aviao(self):
    # Configurações da interface gráfica
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('purple')

    # Criar uma nova janela
    nova_janela = customtkinter.CTk()
    nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 400))
    nova_janela.title("Tela Avião")

    dados = {}

    def confirmar():
        nonlocal dados
        modelo = entry_modelo.get().strip().upper()
        fileiras = entry_fileiras.get().strip()
        assentos_por_fileira = entry_assentos.get().strip()

        # Validar os dados
        if not modelo:
            label_mensagem = customtkinter.CTkLabel(master=frame, text="Modelo inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=30)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        if not fileiras or not fileiras.isdigit():
            label_mensagem = customtkinter.CTkLabel(master=frame, text="Número de fileiras inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        if not assentos_por_fileira or not assentos_por_fileira.isdigit():
            label_mensagem = customtkinter.CTkLabel(master=frame, text="Número de assentos por fileira inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        # Armazenar os dados
        dados["modelo"] = modelo
        dados["fileiras"] = int(fileiras)
        dados["assentos_por_fileira"] = int(assentos_por_fileira)

        label_mensagem = customtkinter.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
        label_mensagem.pack(pady=50)
        nova_janela.update_idletasks()
        nova_janela.after(1000, nova_janela.destroy(), lambda: self.mostra_opcoes())

    frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='purple')
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Inserir Dados do Avião", font=('Tahoma', 20))
    label.pack(pady=12, padx=10)

    entry_modelo = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o modelo", width=200)
    entry_modelo.pack(pady=5)

    entry_fileiras = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o número de fileiras", width=200)
    entry_fileiras.pack(pady=5)

    entry_assentos = customtkinter.CTkEntry(master=frame, placeholder_text="Digite o número de assentos por fileira", width=200)
    entry_assentos.pack(pady=5)

    button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
    button_confirmar.pack(pady=10)

    nova_janela.mainloop()

    return dados

import customtkinter as ctk

def altera_dados_passageiro(self):
    # Configurações da interface gráfica
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')

    # Criar uma nova janela
    nova_janela = ctk.CTk()
    nova_janela.geometry(self.centralizar_janela(nova_janela, 500, 600))
    nova_janela.title("Tela Passageiro")

    dados = {}

    def confirmar():
        nonlocal dados
        nome = entry_nome.get().strip()
        cpf = entry_cpf.get().strip()
        idade = entry_idade.get().strip()
        telefone = entry_telefone.get().strip()

        # Validar os dados
        if not nome:
            label_mensagem = ctk.CTkLabel(master=frame, text="Nome inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=30)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        try:
            int(cpf)
        except ValueError:
            label_mensagem = ctk.CTkLabel(master=frame, text="CPF inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        if not idade:
            label_mensagem = ctk.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        try:
            int(idade)
        except ValueError:
            label_mensagem = ctk.CTkLabel(master=frame, text="Idade inválida, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(4000, lambda: label_mensagem.destroy())
            return

        try:
            int(telefone)
        except ValueError:
            label_mensagem = ctk.CTkLabel(master=frame, text="Telefone inválido, digite novamente!", font=('Tahoma', 12))
            label_mensagem.pack(pady=10)
            label_mensagem.after(1000, lambda: label_mensagem.destroy())
            return

        # Armazenar os dados
        dados["nome"] = nome
        dados["cpf"] = cpf
        dados["idade"] = idade
        dados["telefone"] = telefone

        label_mensagem = ctk.CTkLabel(master=frame, text="Dados inseridos com sucesso!", font=('Tahoma', 20))
        label_mensagem.pack(pady=50)
        nova_janela.update_idletasks()
        nova_janela.after(1000, nova_janela.destroy(), lambda: self.mostra_opcoes())

    frame = ctk.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = ctk.CTkLabel(master=frame, text="Alterar Dados do Passageiro", font=('Tahoma', 20))
    label.pack(pady=12, padx=10, fill='both', expand=True)

    entry_nome = ctk.CTkEntry(master=frame, placeholder_text="Digite o nome", width=200)
    entry_nome.pack(pady=5)

    entry_cpf = ctk.CTkEntry(master=frame, placeholder_text="Digite o CPF", width=200)
    entry_cpf.pack(pady=5)

    entry_idade = ctk.CTkEntry(master=frame, placeholder_text="Digite a idade", width=200)
    entry_idade.pack(pady=5)

    entry_telefone = ctk.CTkEntry(master=frame, placeholder_text="Digite o telefone", width=200)
    entry_telefone.pack(pady=5)

    button_confirmar = ctk.CTkButton(master=frame, text="Confirmar", command=confirmar, width=10)
    button_confirmar.pack(pady=10)

    nova_janela.mainloop()

    return dados


import string
from typing import TypedDict
from telas.abstractTela import AbstractTela
from entidades.voo import Voo
import customtkinter


class DadosIncluiReserva(TypedDict):
    fileira: int
    letra: str
    cpf_passageiro: str
    codigo_voo: str


class TelaReservas(AbstractTela):
    def __init__(self):
        super().__init__(
            {
                1: "Incluir Reserva",
                2: "Alterar Reserva",
                3: "Excluir Reserva",
                4: "Listar Reservas",
                0: "Retornar",
            }
        )

    def mostra_opcoes(self) -> int:
        # Configurações da interface gráfica
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # Criar uma nova janela
        nova_janela = customtkinter.CTk()
        nova_janela.geometry('500x600')
        nova_janela.title("Tela Reservas")

        opcao_selecionada = None

        def set_opcao_selecionada(index: int):
            nonlocal opcao_selecionada
            opcao_selecionada = index
            nova_janela.destroy()

        frame = customtkinter.CTkFrame(master=nova_janela, corner_radius=20, border_width=4, border_color='green')
        frame.pack(pady=20, padx=60, fill='both', expand=True)

        label = customtkinter.CTkLabel(master=frame, text="RESERVAS", font=('Tahoma', 20))
        label.pack(pady=12, padx=10)

        for index, opcao in self.opcoes.items():
            button = customtkinter.CTkButton(master=frame, text=opcao, command=lambda index=index: set_opcao_selecionada(index))
            button.pack(pady=12, padx=10)

        nova_janela.mainloop()

        return opcao_selecionada

    def pega_cpf(self, alterando=False):
        while True:
            try:
                cpf = input("Digite o CPF do passageiro: ").strip()

                if not cpf and alterando:
                    return cpf

                self.verica_cpf(cpf)
                return cpf

            except Exception as e:
                print(str(e))

    def verica_cpf(self, cpf):
        if not cpf.isdigit():
            raise Exception("O CPF deve ser composto por dígitos!")

    def pega_voo(self):
        while True:
            codigo_voo = input("Digite o código do Voo: ").upper().strip()

            if codigo_voo:
                return codigo_voo

            else:
                print("Dado invalido, digite novamente!!!")

    def pega_fileira(self, alterando=False):
        while True:
            try:
                fileira = input("Digite o número da fileira desejada: ").strip()

                if not fileira and alterando:
                    return 0

                if not fileira:
                    raise Exception("O campo nao pode ser vazio!")

                if not fileira.isdigit():
                    raise Exception("A fileira deve ser composta por números!")

                if int(fileira) < 1:
                    raise Exception("A fileira deve ser maior que 1!")

                return int(fileira)

            except Exception as e:
                print(str(e))

    def pega_assento_fileira(self, alterando=False):
        while True:
            try:
                assento = input("Digite a letra do assento desejado: ").upper().strip()

                if not assento and alterando:
                    return ""

                if not assento:
                    raise Exception("O campo nao pode ser vazio!")

                if assento not in string.ascii_uppercase:
                    raise Exception("O campo assento deve ser uma letra!")

                return assento

            except Exception as e:
                print(str(e))

    def mostra_reserva(self, dados_reserva: "dict[str, str]"):
        for chave, valor in dados_reserva.items():
            print(f"{chave}: {valor}")

        print("\n")

    def mostra_assentos_voo(self, voo: Voo):
        print("{:<1} ".format(""), end="")

        for i in range(voo.aviao.assentos_por_fileira):
            print("[{:^1}] | ".format(string.ascii_uppercase[i]), end="")
        print()

        for i in range(voo.aviao.fileiras):
            print("{} ".format(i + 1), end="")

            for j in range(voo.aviao.assentos_por_fileira):
                print("[{:^1}] | ".format(voo.assentos[i][j]), end="")

            print()

    def seleciona_reserva(self) -> str:
        codigo_reserva = (
            input("Insira o código da reserva que deseja buscar: ").upper().strip()
        )

        return codigo_reserva
