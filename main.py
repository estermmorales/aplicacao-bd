import database as db
import time
menu_principal = """
---------CENTRO DE DISTRIBUIÇÃO----------
Selecione uma opção...

1) Criar tabelas
2) Deletar tabelas
----------------OPERAÇÕES----------------
3) Inserir
4) Exibir
5) Atualizar
6) Excluir
------------------------------------------
7) Consultas avançadas
------------------------------------------
8) Sair
------------------------------------------
Sua opção: 
"""
menu_opcoes = """
1) Loja
2) Agência
3) Cliente
4) Emitente/Destinario
5) Funcionario
6) Usuário
7) Protocolo
----------------------------------------
8) Cancelar
----------------------------------------
Sua opção: 
"""

def cadastro():
    print("\n----------------INSERIR----------------")
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
    print("\n----------------EXIBIR----------------")
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

def atualizar():
    print("\n----------------ATUALIZAR----------------")
    while (opcao :=input(menu_opcoes)) !=8:
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
                print("Opcão inválida")
                
def excluir():
    print("\n----------------EXCLUIR----------------")
    while (opcao :=input(menu_opcoes)) !=8:
            if opcao == "1":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "2":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "3":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "4":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "5":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "6":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            elif opcao == "7":
                exc = input("Deseja mesmo excluir? S/N")
                if (exc == "S"):
                    pass
            else:
                print("Opção inválida")
                
while (opcao := input(menu_principal)) != "8":
    if opcao == "1":
        db.create_all_tables()
        time.sleep(1.5)
    elif opcao == "2":
        db.drop_all_tables()
        time.sleep(1.5)
    elif opcao == "3":
        cadastro()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        atualizar()
    elif opcao == "6":
        excluir()
    elif opcao == "7":
        pass
    else:
        print("Opção inválida")