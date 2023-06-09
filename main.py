import time
import database as db
from database import mydb

menu_principal = """
---------CENTRO DE DISTRIBUIÇÃO----------
Selecione uma opção...

1) Criar tabelas
2) Inserir valores iniciais nas tabelas
3) Deletar tabelas
----------------OPERAÇÕES----------------
4) Inserir
5) Exibir
6) Atualizar
7) Excluir
------------------------------------------
8) Consultas avançadas
------------------------------------------
9) Sair
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
menu_consultas_avancadas = """
----------CONSULTAS AVANÇADAS------------
1) Gerar a soma de volumes por usuário responsável
2) Agrupar e soma os protocolos por destinatário
3) Agrupar os protocolos por situação
----------------------------------------
4) Cancelar
----------------------------------------
Sua opção: 
"""


def inserir():
    print("\n----------------INSERIR----------------")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            db.insert('loja')
        elif opcao == "2":
            db.insert('agencia')
        elif opcao == "3":
            db.insert('cliente')
        elif opcao == "4":
            db.insert('emitente_destinatario')
        elif opcao == "5":
            db.insert('funcionario')
        elif opcao == "6":
            db.insert('usuario')
        elif opcao == "7":
            db.insert('protocolo')
        else:
            print("Opção inválida")


def listar():
    print("\n----------------EXIBIR----------------")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            db.read('loja')
            time.sleep(1.5)
        elif opcao == "2":
            db.read('agencia')
            time.sleep(1.5)
        elif opcao == "3":
            db.read('cliente')
            time.sleep(1.5)
        elif opcao == "4":
            db.read('emitente_destinatario')
            time.sleep(1.5)
        elif opcao == "5":
            db.read('funcionario')
            time.sleep(1.5)
        elif opcao == "6":
            db.read('usuario')
            time.sleep(1.5)
        elif opcao == "7":
            db.read('protocolo')
            time.sleep(1.5)
        else:
            print("Opção inválida")


def atualizar():
    print("\n----------------ATUALIZAR----------------")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            db.update('loja')
        elif opcao == "2":
            db.update('agencia')
        elif opcao == "3":
            db.update('cliente')
        elif opcao == "4":
            db.update('emitente_destinatario')
        elif opcao == "5":
            db.update('funcionario')
        elif opcao == "6":
            db.update('usuario')
        elif opcao == "7":
            db.update('protocolo')
        else:
            print("Opcão inválida")


def excluir():
    print("\n----------------EXCLUIR----------------")
    while (opcao := input(menu_opcoes)) != "8":
        if opcao == "1":
            db.delete('loja')
        elif opcao == "2":
            db.delete('agencia')
        elif opcao == "3":
            db.delete('cliente')
        elif opcao == "4":
            db.delete('emitente_destinatario')
        elif opcao == "5":
            db.delete('funcionario')
        elif opcao == "6":
            db.delete('usuario')
        elif opcao == "7":
            db.delete('protocolo')
        else:
            print("Opção inválida")


def consultas_avançadas():
    while (opcao := input(menu_consultas_avancadas)) != "4":
        if opcao == "1":
            db.consulta_avancada1()
        elif opcao == "2":
            db.consulta_avancada2()
        elif opcao == "3":
            db.consulta_avancada3()
        else:
            print("Opção inválida")


while (opcao := input(menu_principal)) != "9":
    if opcao == "1":
        db.create_all_tables()
        time.sleep(1.5)
    elif opcao == "2":
        db.insert_on_tables()
        time.sleep(1.5)
    elif opcao == "3":
        db.drop_all_tables()
        time.sleep(1.5)
    elif opcao == "4":
        inserir()
        time.sleep(1.5)
    elif opcao == "5":
        listar()
        time.sleep(1.5)
    elif opcao == "6":
        atualizar()
        time.sleep(1.5)
    elif opcao == "7":
        excluir()
        time.sleep(1.5)
    elif opcao == "8":
        consultas_avançadas()
        time.sleep(1.5)
    else:
        print("Opção inválida")
