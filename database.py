from dotenv import load_dotenv
import mysql.connector as conn
from mysql.connector import errorcode
import os

load_dotenv()
try:
    mydb = conn.connect(
        host="localhost",
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database"),
        autocommit=False
    ) 
except conn.Error as error:
    print("Erro ao se conectar ao banco de dados {}".format(error))


# Criação das tabelas
tables = {}
tables['agencia'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`agencia` (
  `Documento` DECIMAL(10,0) NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `Dcumento` (`Documento` ASC) VISIBLE);
"""
tables['cliente'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`cliente` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE);
"""
tables['emitente_destinatario'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`emitente_destinatario` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE);
"""
tables['funcionario'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`funcionario` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE);
"""
tables['loja'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`loja` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE);
"""
tables['perfil'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`perfil` (
  `id` INT(11) NOT NULL,
  `id_permissao` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`));
"""
tables['permissoes'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`permissoes` (
  `id` INT(11) NOT NULL,
  `Nome` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`));
"""
tables['pessoas'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`pessoas` (
  `id` INT(11) NOT NULL,
  `Nome` VARCHAR(40) NULL DEFAULT NULL,
  `id_loja` INT(11) NULL DEFAULT NULL,
  `id_cliente` INT(11) NULL DEFAULT NULL,
  `id_funcionario` INT(11) NULL DEFAULT NULL,
  `id_agencia` INT(11) NULL DEFAULT NULL,
  `id_remetente_destinatario` INT(11) NULL DEFAULT NULL,
  `telefone` DOUBLE NULL DEFAULT NULL,
  `e_mail` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_pessoas_2` (`id_remetente_destinatario` ASC) VISIBLE,
  INDEX `FK_pessoas_3` (`id_funcionario` ASC) VISIBLE,
  INDEX `FK_pessoas_4` (`id_cliente` ASC) VISIBLE,
  INDEX `FK_pessoas_5` (`id_loja` ASC) VISIBLE,
  INDEX `FK_pessoas_6` (`id_agencia` ASC) VISIBLE,
  CONSTRAINT `FK_pessoas_2`
    FOREIGN KEY (`id_remetente_destinatario`)
    REFERENCES `centro_de_distribuicao`.`emitente_destinatario` (`id`),
  CONSTRAINT `FK_pessoas_3`
    FOREIGN KEY (`id_funcionario`)
    REFERENCES `centro_de_distribuicao`.`funcionario` (`id`),
  CONSTRAINT `FK_pessoas_4`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `centro_de_distribuicao`.`cliente` (`id`),
  CONSTRAINT `FK_pessoas_5`
    FOREIGN KEY (`id_loja`)
    REFERENCES `centro_de_distribuicao`.`loja` (`id`),
  CONSTRAINT `FK_pessoas_6`
    FOREIGN KEY (`id_agencia`)
    REFERENCES `centro_de_distribuicao`.`agencia` (`id`));
"""
tables['usuario'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`usuario` (
  `id` INT(11) NOT NULL,
  `nome` VARCHAR(40) NULL DEFAULT NULL,
  `senha` VARCHAR(40) NULL DEFAULT NULL,
  `id_perfil` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `usuario_perfil` (`id_perfil` ASC) VISIBLE,
  CONSTRAINT `usuario_perfil`
    FOREIGN KEY (`id_perfil`)
    REFERENCES `centro_de_distribuicao`.`perfil` (`id`));
"""
tables['situacao'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`situacao` (
  `id` INT(11) NOT NULL,
  `Nome` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`));
"""
tables['protocolo'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`protocolo` (
  `id` INT(11) NOT NULL,
  `qtd_volumes` INT(11) NULL DEFAULT NULL,
  `id_usuario_responsavel` INT(11) NULL DEFAULT NULL,
  `Observacao` VARCHAR(40) NULL DEFAULT NULL,
  `id_situacao` INT(11) NULL DEFAULT NULL,
  `dt_entrega` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dt_retirada` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  `id_pessoa_remetente` INT(11) NULL DEFAULT NULL,
  `id_pessoa_destinatario` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_Protocolo_2` (`id_usuario_responsavel` ASC) VISIBLE,
  INDEX `FK_Protocolo_3` (`id_situacao` ASC) VISIBLE,
  INDEX `id_pessoas_remetente` (`id_pessoa_remetente` ASC) VISIBLE,
  INDEX `id_pessoas_destinatario` (`id_pessoa_destinatario` ASC) VISIBLE,
  CONSTRAINT `FK_Protocolo_2`
    FOREIGN KEY (`id_usuario_responsavel`)
    REFERENCES `centro_de_distribuicao`.`usuario` (`id`),
  CONSTRAINT `FK_Protocolo_3`
    FOREIGN KEY (`id_situacao`)
    REFERENCES `centro_de_distribuicao`.`situacao` (`id`),
  CONSTRAINT `id_pessoas_destinatario`
    FOREIGN KEY (`id_pessoa_destinatario`)
    REFERENCES `centro_de_distribuicao`.`pessoas` (`id`)
    ON DELETE SET NULL,
  CONSTRAINT `id_pessoas_remetente`
    FOREIGN KEY (`id_pessoa_remetente`)
    REFERENCES `centro_de_distribuicao`.`pessoas` (`id`)
    ON DELETE SET NULL);
"""
# Exclusão das tabelas
drop_tables = """
drop tables situacao, protocolo, pessoas, permissoes, perfil, loja, funcionario, emitente_destinatario, cliente, agencia, usuario;
"""
#Função para criar todas as tabelas
def create_all_tables():
    try:
        cursor = mydb.cursor()
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Criando tabela {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except conn.Error as error:
                if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Tabela já existe.")
                else:
                    print(error.msg)
            else:
                print("OK")
    except conn.Error as error:
        print("Ocorreu um erro durante o processamento {}.".format(error))
    finally:
        if mydb.is_connected():
            cursor.close()  
#Função para excluir todas as tabelas
def drop_all_tables():
    try:
        cursor = mydb.cursor()
        print("Excluindo tabelas...")
        cursor.execute(drop_tables)
    except conn.Error as error:
        print(error.msg)
    else:
        print("OK")
    finally:
        if mydb.is_connected():
            cursor.close()  


