from dotenv import load_dotenv
import mysql.connector as conn
import os

clear = lambda: os.system('cls')
load_dotenv()
mydb = conn.connect(
    host="localhost",
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
) 

menu_principal = """
Menu Principal
Selecione uma opção
1) Cadastrar
2) Exibir
3) Atualizar
4) Excluir
5) Consultas avançadas
6) Sair
"""

menu_opcoes = """
1) Loja
2) Agência
3) Cliente
4) Emitente/Destinario
5) Funcionario
6) Usuário
7) Protocolo
8) Cancelar
"""

def cadastro():
    print("\nCadastrar novo(a)...")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            pass
        elif opcao == "7":
            pass
        else:
            print("Opção inválida")


def listar():
    print("\nSelecione o que exibir...")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "Sim"):
                pass
        elif opcao == "2":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        elif opcao == "3":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        elif opcao == "4":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        elif opcao == "5":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        elif opcao == "6":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        elif opcao == "7":
            filtro = input("Deseja filtrar? S/N ")
            if (filtro == "S"):
                pass
        else:
            print("Opção inválida")

while (opcao := input(menu_principal)) != "6":
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    else:
        print("Opção inválida")


