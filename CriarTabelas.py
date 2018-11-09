import pymysql as mysql

def criarTabelaClientes():
    connection = mysql.connect("localhost", "root", "", "quartoanoinfo")
    cursor = connection.cursor()

    sql = """CREATE TABLE clientes (IdClientes INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(255), cpf VARCHAR(30), email VARCHAR(255), telefone VARCHAR(30))"""

    cursor.execute(sql)
    connection.close()

def criarTabelaProdutos():
    connection = mysql.connect("localhost", "root", "", "quartoanoinfo")
    cursor = connection.cursor()

    sql = """CREATE TABLE produtos (IdProdutos INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, codigo VARCHAR(30), descricao VARCHAR(255), unidade VARCHAR(5), prcCompra DOUBLE, prcVis DOUBLE)"""

    cursor.execute(sql)
    connection.close()