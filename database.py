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
        database="centro_de_distribuicao",
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
  UNIQUE INDEX `Dcumento` (`Documento` ASC) VISIBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['cliente'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`cliente` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['emitente_destinatario'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`emitente_destinatario` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['funcionario'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`funcionario` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['loja'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`loja` (
  `documento` DOUBLE NULL DEFAULT NULL,
  `id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `documento` (`documento` ASC) VISIBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['perfil'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`perfil` (
  `id` INT(11) NOT NULL,
  `id_permissao` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['permissoes'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`permissoes` (
  `id` INT(11) NOT NULL,
  `Nome` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
    REFERENCES `centro_de_distribuicao`.`agencia` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
    REFERENCES `centro_de_distribuicao`.`perfil` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['situacao'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`situacao` (
  `id` INT(11) NOT NULL,
  `Nome` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
tables['protocolo'] = """
CREATE TABLE IF NOT EXISTS `centro_de_distribuicao`.`protocolo` (
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
  KEY `FK_Protocolo_2` (`id_usuario_responsavel`),
  KEY `FK_Protocolo_3` (`id_situacao`),
  KEY `id_pessoas_remetente` (`id_pessoa_remetente`),
  KEY `id_pessoas_destinatario` (`id_pessoa_destinatario`),
  CONSTRAINT `FK_Protocolo_2` FOREIGN KEY (`id_usuario_responsavel`) REFERENCES `usuario` (`id`),
  CONSTRAINT `FK_Protocolo_3` FOREIGN KEY (`id_situacao`) REFERENCES `situacao` (`id`),
  CONSTRAINT `id_pessoas_destinatario` FOREIGN KEY (`id_pessoa_destinatario`) REFERENCES `pessoas` (`id`) ON DELETE SET NULL,
  CONSTRAINT `id_pessoas_remetente` FOREIGN KEY (`id_pessoa_remetente`) REFERENCES `pessoas` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
"""
# Exclusão das tabelas
drop_tables = """
drop tables situacao, protocolo, pessoas, permissoes, perfil, loja, funcionario, emitente_destinatario, cliente, agencia, usuario;
"""
#Inserir valores nas tabelas
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
    #Dando erro em dt_retirada
    'protocolo': (
        """
        INSERT INTO `protocolo` VALUES (1,1,1,NULL,1,'2023-05-24 19:02:00',NULL,2,4),(2,1,1,NULL,1,'2023-05-24 19:02:00',NULL,2,3),(3,2,2,NULL,3,'2023-05-25 13:43:10',NULL,3,2),(4,1,2,NULL,2,'2023-05-25 13:43:10',NULL,4,3);
        """
    )
    }
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

#CRUD
def insert(table_name):
    pass

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

def update():
    pass

def delete():
    pass

#Consultas avançadas

def consulta_avancada1():
    cursor = mydb.cursor()
    select = """
    select sum(pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO, u.nome as RESPONSAVEL
    FROM protocolo pt 
    JOIN usuario u on pt.id_usuario_responsavel = u.id
    join situacao s on pt.id_situacao = s.id
    group by pt.id_usuario_responsavel;
    """
    cursor.execute(select)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
 
def consulta_avancada2():
    cursor = mydb.cursor()
    select = """
    select count(pt.id) as REGISTROS, sum( pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO
    FROM protocolo pt 
    join pessoas pd on pd.id= pt.id_pessoa_destinatario
    join situacao s on pt.id_situacao = s.id
    group by pt.id_pessoa_remetente;
    """ 
    cursor.execute(select)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

def consulta_avancada3():
    cursor = mydb.cursor()
    select = """
    select count(pt.id) as REGISTROS, sum( pt.qtd_volumes) as VOLUMES, pt.dt_entrega as ENTREGA, s.nome as SITUACAO
    FROM protocolo pt 
    join pessoas pd on pd.id= pt.id_pessoa_destinatario
    join situacao s on pt.id_situacao = s.id
    group by s.id;
    """
    cursor.execute(select)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
