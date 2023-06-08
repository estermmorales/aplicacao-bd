from dotenv import load_dotenv
import mysql.connector as conn
from mysql.connector import errorcode
import os
import datetime as dt

# Conexão com o banco de dados
load_dotenv()
try:
    mydb = conn.connect(
        host="localhost",
        user=os.getenv("user"),
        password=os.getenv("password"),
        database="centro_de_distribuicao",
        autocommit=False
    )
except conn.Error as error:
    print("Erro ao se conectar ao banco de dados {}".format(error))

# Criação das tabelas
tables = {}
tables['agencia'] = """
CREATE TABLE `agencia` (
  `Documento` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Dcumento` (`Documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['cliente'] = """
CREATE TABLE `cliente` (
  `documento` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['emitente_destinatario'] = """
CREATE TABLE `emitente_destinatario` (
  `documento` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['funcionario'] = """
CREATE TABLE `funcionario` (
  `documento` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['loja'] = """
CREATE TABLE `loja` (
  `documento` varchar(14) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['perfil'] = """
CREATE TABLE `perfil` (
  `id` int(11) NOT NULL,
  `id_permissao` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['permissoes'] = """
CREATE TABLE `permissoes` (
  `id` int(11) NOT NULL,
  `Nome` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['pessoas'] = """
CREATE TABLE `pessoas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(40) DEFAULT NULL,
  `id_loja` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_funcionario` int(11) DEFAULT NULL,
  `id_agencia` int(11) DEFAULT NULL,
  `id_remetente_destinatario` int(11) DEFAULT NULL,
  `telefone` double DEFAULT NULL,
  `e_mail` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_loja_idx` (`id_loja`),
  KEY `id_emitente_destinatario_idx` (`id_remetente_destinatario`),
  KEY `id_funcionario_idx` (`id_funcionario`),
  KEY `id_cliene_idx` (`id_cliente`),
  KEY `id_agencia_idx` (`id_agencia`),
  CONSTRAINT `id_agencia` FOREIGN KEY (`id_agencia`) REFERENCES `agencia` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_emitente_destinatario` FOREIGN KEY (`id_remetente_destinatario`) REFERENCES `emitente_destinatario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_loja` FOREIGN KEY (`id_loja`) REFERENCES `loja` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['usuario'] = """
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(40) DEFAULT NULL,
  `senha` varchar(40) DEFAULT NULL,
  `id_perfil` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_perfil` (`id_perfil`),
  CONSTRAINT `usuario_perfil` FOREIGN KEY (`id_perfil`) REFERENCES `perfil` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['situacao'] = """
CREATE TABLE `situacao` (
  `id` int(11) NOT NULL,
  `Nome` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['protocolo'] = """
CREATE TABLE `protocolo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qtd_volumes` int(11) DEFAULT NULL,
  `id_usuario_responsavel` int(11) DEFAULT NULL,
  `Observacao` varchar(40) DEFAULT NULL,
  `id_situacao` int(11) DEFAULT NULL,
  `dt_entrega` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dt_retirada` timestamp NULL DEFAULT NULL,
  `id_pessoa_remetente` int(11) DEFAULT NULL,
  `id_pessoa_destinatario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `situacao` (`id_situacao`),
  KEY `id_pessoa_remetente_idx` (`id_pessoa_remetente`),
  KEY `id_pessoa_destinatario_idx` (`id_pessoa_destinatario`),
  KEY `id_usuario_idx` (`id_usuario_responsavel`),
  CONSTRAINT `id_pessoa_destinatario` FOREIGN KEY (`id_pessoa_destinatario`) REFERENCES `pessoas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_pessoa_remetente` FOREIGN KEY (`id_pessoa_remetente`) REFERENCES `pessoas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario_responsavel`) REFERENCES `usuario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `situacao` FOREIGN KEY (`id_situacao`) REFERENCES `situacao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

# Exclusão das tabelas
drop_tables = """
drop tables situacao, protocolo, pessoas, permissoes, perfil, loja, funcionario, emitente_destinatario, cliente, agencia, usuario;
"""

# Inserir valores nas tabelas
inserts = {
    'agencia': (
        """
    INSERT INTO `agencia` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
    """),
    'cliente': (
        """
        INSERT INTO `cliente` VALUES (100000000002,2),(100000000003,3),(100000000004,4),(100000000005,5);
        """
    ),
    'emitente_destinatario': (
        """
        INSERT INTO `emitente_destinatario` VALUES (200000000002,2),(200000000003,3),(200000000004,4),(200000000005,5),(200000000006,6),(200000000007,7),(200000000008,8),(200000000009,9),(200000000010,10);
        """
    ),
    'funcionario': (
        """
        INSERT INTO `funcionario` VALUES (300000000002,2),(300000000003,3),(300000000004,4),(300000000005,5),(300000000006,6),(300000000007,7),(300000000008,8),(300000000009,9),(300000000010,10);
        """
    ),
    'loja': (
        """
        INSERT INTO `loja` VALUES (400000000002,2),(400000000003,3),(400000000004,4),(400000000005,5),(400000000006,6),(400000000007,7),(400000000008,8),(400000000009,9),(400000000010,10);
        """
    ),
    'perfil': (
        """
        INSERT INTO `perfil` VALUES (1,10),(2,20),(3,30),(4,40);
        """
    ),
    'permissoes': (
        """
        INSERT INTO `permissoes` VALUES (10,'Gerente'),(20,'Estagiáro'),(30,'Funcionário'),(40,'Visitante');
        """
    ),
    'pessoas': (
        """
        INSERT INTO `pessoas` VALUES (1,'João da Silva',NULL,2,NULL,NULL,NULL,4899898,'joaosadilva@gmail.com'),(2,'Bela Maria',3,NULL,NULL,NULL,NULL,4899898,'belamaria@gmail.com'),(3,'Correios',NULL,NULL,NULL,NULL,2,4899898,'correios@gmail.com'),(4,'Jorgete Souza',NULL,NULL,4,NULL,NULL,4899898,'jorgete@gmail.com'),(5,'Zezinho Turismo',NULL,NULL,NULL,3,NULL,4899898,'zezinhotur@gmail.com'),(6,'Marilia Costa',NULL,3,NULL,NULL,NULL,4899898,'mariliacosta@gmail.com'),(7,'Francisco Mendes',NULL,4,NULL,NULL,NULL,4899898,'joaosadilva@gmail.com'),(8,'Gata Dengosa',8,NULL,NULL,NULL,NULL,48999655555,'gatadengosa@gmail.com'),(9,'Xiquita Bacana',2,NULL,NULL,NULL,NULL,48999991111,'xiquitabacana@gmail.com'),(10,'Gata Malhada',4,NULL,NULL,NULL,NULL,48999222222,'gatamalhada@mail.com'),(11,'Gata Ousada',5,NULL,NULL,NULL,NULL,48999993323,'gataousada@gmail.com'),(12,'Mais Mulher',6,NULL,NULL,NULL,NULL,4888882222,'mailmulher@gmail.com'),(13,'Eu Fashion ',7,NULL,NULL,NULL,NULL,48955555555,'eeufashion@gmail.com'),(14,'DuHomem',9,NULL,NULL,NULL,NULL,4888778877,'duhomem@gmail.com'),(15,'Casa Show',10,NULL,NULL,NULL,NULL,48922222222,'casashow@gmail.com'),(16,'Julia Maria',NULL,5,NULL,NULL,NULL,48999221122,'juliamaria@gmail.com'),(17,'Simão Tur',NULL,NULL,NULL,1,NULL,48999885555,'simaotur@gmail.com'),(18,'Mari Tur',NULL,NULL,NULL,2,NULL,48988558855,'maritur@gmail.com'),(19,'Laci Tur',NULL,NULL,NULL,4,NULL,48988778877,'lacitur@gmail.com'),(20,'Vagens da Zo',NULL,NULL,NULL,5,NULL,48955336666,'viagenszo@gmail.com'),(21,'Expresso São Miguel',NULL,NULL,NULL,NULL,3,48999995566,'saomiguel@gmail.com'),(22,'Bauer Transportes',NULL,NULL,NULL,NULL,4,4888888888,'bauertur@gmail.com'),(23,'ifood',NULL,NULL,NULL,NULL,5,4822332233,'ifood@gmail.com'),(24,'Marmitex da Ana',NULL,NULL,NULL,NULL,6,48955225522,'marmitexana@gmail.com'),(25,'Jessica Regina',NULL,NULL,2,NULL,NULL,48925556555,'jessia@gmail.com.br'),(26,'João Mendes',NULL,NULL,3,NULL,NULL,48954666966,'joao@gmail.com'),(27,'Juca Luan',NULL,NULL,5,NULL,NULL,4899889988,'juca@gmail.com'),(28,'Marlize Joaquim',NULL,NULL,6,NULL,NULL,4965666555,'marlize@gmail.com');
        """
    ),
    'usuario': (
        """
        INSERT INTO `usuario` VALUES (1,'ana','ana',1),(2,'maria','maria',2),(3,'julia','julia',3),(4,'carol','carol',4),(5,'fernanda','fernanda',2),(6,'jessi','jessi',3),(7,'gustavo','gustavo',2);
        """
    ),
    'situacao': (
        """
        INSERT INTO `situacao` VALUES (1,'PENDENTE'),(2,'RETIRADO'),(3,'CANCELADO');
        """
    ),
    'protocolo': (
        """
        INSERT INTO `protocolo` VALUES (1,1,1,NULL,1,'2023-05-24 19:02:00',NULL,2,4),(2,1,1,NULL,1,'2023-05-24 19:02:00',NULL,2,3),(3,2,2,NULL,3,'2023-05-25 13:43:10',NULL,3,2),(4,1,2,NULL,2,'2023-05-25 13:43:10',NULL,4,3);
        """
    )
}


# Função para criar todas as tabelas
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


# Função para excluir todas as tabelas
def drop_all_tables():
    try:
        cursor = mydb.cursor()
        print("Excluindo tabelas: ".format(), end='')
        cursor.execute(drop_tables)
    except conn.Error as error:
        print(error.msg)
    else:
        print("OK")
    finally:
        if mydb.is_connected():
            cursor.close()


# Inserção dos valores nas tabelas
def insert_on_tables():
    cursor = mydb.cursor()
    for insert_name in inserts:
        insert_description = inserts[insert_name]
        try:
            print("Inserindo valores para {}: ".format(insert_name), end='')
            cursor.execute(insert_description)
        except conn.Error as error:
            print(error.msg)
        else:
            print("OK")
    mydb.commit()
    cursor.close()


# CRUD
def insert(table_name):
    try:
        cursor = mydb.cursor()
        if table_name == 'usuario':
            nome_insert = input("Nome: ")
            senha_insert = input("Senha: ")
            id_perfil_insert = input("Id Perfil: ")
            query = [
                f"INSERT INTO {table_name}(nome, senha, id_perfil) VALUES ('{nome_insert}', '{senha_insert}', '{id_perfil_insert}')"]
        elif table_name == 'protocolo':
            qtd_volumes = input("Quantidade Volumes: ")
            id_usuario_responsavel = input("Id do usuário responsável: ")
            id_situacao = input("Id Situação: ")
            dt = dt.datetime.now()
            dt_entrega = dt.replace(tzinfo=None)
            id_pessoa_remetente = input("Id do remetente:")
            id_pessoa_destinatario = input("Id do destinatário: ")
            query = [f"INSERT INTO {table_name} (qtd_volumes, id_usuario_responsavel, id_situacao, dt_entrega, id_pessoa_remetente, id_pessoa_destinatario) VALUES ('{qtd_volumes}', '{id_usuario_responsavel}', '{id_situacao}', '{dt_entrega}', '{id_pessoa_remetente}', '{id_pessoa_destinatario}')"]
        else:
            documento = input("Documento: ")
            query = [
                f"INSERT INTO {table_name} (documento) VALUES ({documento})"]
        sql = ''.join(query)
        cursor.execute(sql)
    except conn.Error as error:
        print(error.msg)
    else:
        print("Atributo adicionado")
        mydb.commit()
        cursor.close()


def read(table_name):
    try:
        cursor = mydb.cursor()
        select = "select * from " + table_name
        cursor.execute(select)
    except conn.Error as error:
        print(error.msg)
    else:
        print("TABELA {}".format(table_name))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    cursor.close()


def update(table_name):
    try:
        cursor = mydb.cursor()
        atributo = input("Digite o atributo a ser alterado: ")
        valor = input("Digite o valor a ser atribuido: ")
        variavel = input("Digite a variavel: ")
        variavel_valor = input("Digite o valor da variavel: ")
        query = [
            f"UPDATE {table_name} SET {atributo} = {valor} WHERE {variavel} = {variavel_valor}"]
        sql = ''.join(query)
        cursor.execute(sql)
    except conn.Error as error:
        print(error.msg)
    else:
        print("Atributo atualizado")
        mydb.commit()
        cursor.close()


def delete(table_name):
    try:
        cursor = mydb.cursor()
        variavel = input("Digite a variavel: ")
        variavel_valor = input("Digite o valor da variavel: ")
        query = [
            f"DELETE FROM {table_name} WHERE {variavel} = {variavel_valor}"]
        sql = ''.join(query)
        cursor.execute(sql)
    except conn.Error as error:
        print(error.msg)
    else:
        print("Atributo excluído")
        mydb.commit()
        cursor.close()


# Consultas avançadas
# Caso dê erro ao rodar as consultas avançadas, use SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY','')); no Workbench
def consulta_avancada1():
    try:
        cursor = mydb.cursor()
        select = """
        select sum(pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO, u.nome as RESPONSAVEL
        FROM protocolo pt 
        JOIN usuario u on pt.id_usuario_responsavel = u.id
        join situacao s on pt.id_situacao = s.id
        group by pt.id_usuario_responsavel;
        """
        cursor.execute(select)
    except conn.Error as error:
        print(error.msg)
    else:
        myresult = cursor.fetchall()
        print("Gera a soma de volumes por usuário responsável")
        for x in myresult:
            print(
                f"VOLUMES: {x[0]}  |  ENTREGA: {x[1]}  | SITUACAO: {x[2]} |  RESPONSAVEL: {x[3]}")


def consulta_avancada2():
    try:
        cursor = mydb.cursor()
        select = """
        select count(pt.id) as REGISTROS, sum( pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO
        FROM protocolo pt 
        join pessoas pd on pd.id= pt.id_pessoa_destinatario
        join situacao s on pt.id_situacao = s.id
        group by pt.id_pessoa_remetente;
        """
        cursor.execute(select)
    except conn.Error as error:
        print(error.msg)
    else:
        myresult = cursor.fetchall()
        print("Agrupa e soma os protocolos por destinatário")
        for x in myresult:
            print(
                f"REGISTROS: {x[0]}  |  VOLUMES: {x[1]}  | ENTREGA: {x[2]} |  SITUACAO: {x[3]}")


def consulta_avancada3():
    try:
        cursor = mydb.cursor()
        select = """
        select count(pt.id) as REGISTROS, sum( pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO
        FROM protocolo pt 
        join pessoas pd on pd.id= pt.id_pessoa_destinatario
        join situacao s on pt.id_situacao = s.id
        group by s.id;
        """
        cursor.execute(select)
    except conn.Error as error:
        print(error.msg)
    else:
        myresult = cursor.fetchall()
        print("Agrupa os protocolos por situação")
        for x in myresult:
            print(
                f"REGISTROS: {x[0]}  |  VOLUMES: {x[1]}  | ENTREGA: {x[2]} |  SITUACAO: {x[3]}")
