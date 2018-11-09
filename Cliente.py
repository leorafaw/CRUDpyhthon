import pymysql as mysql

class Cliente(object):

    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def CadastrarCliente(Cliente):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor=c.cursor()
        sql = "INSERT INTO clientes(nome, cpf, email, telefone) VALUES(%s, %s, %s, %s)"
        val = (Cliente.nome, Cliente.cpf, Cliente.email, Cliente.telefone)
        cursor.execute(sql, val)
        c.commit()
        c.close()

    def SelecionarUmCliente(Cliente):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor = c.cursor()
        result = []
        sql = "SELECT * FROM clientes WHERE cpf = %s"
        val = (Cliente.cpf)
        cursor.execute(sql, val)
        for i in cursor.fetchall():
            result.append(i)
        c.commit()
        c.close()
        return result