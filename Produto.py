import pymysql as mysql
class Produto(object):

    def  __init__(self, codigo, descricao, unidade, prcCompra, prcVis):
        self.codigo = codigo
        self.descricao = descricao
        self.unidade = unidade
        self.prcCompra = prcCompra
        self.prcVis = prcVis

    def CadastrarProduto(Produto):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor=c.cursor()
        sql = "INSERT INTO produtos(codigo, descricao, unidade, prcCompra, prcVis) VALUES(%s, %s, %s, %s, %s)"
        val = (Produto.codigo, Produto.descricao, Produto.unidade, Produto.prcCompra, Produto.prcVis)
        cursor.execute(sql, val)
        c.commit()
        c.close()

    def AlterarProduto(Produto):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor = c.cursor()
        sql = "UPDATE produtos SET descricao = %s, unidade = %s, prcCompra = %s, prcVis = %s WHERE codigo = %s"
        val = (Produto.descricao, Produto.unidade, Produto.prcCompra, Produto.prcVis, Produto.codigo)
        cursor.execute(sql, val)
        c.commit()
        c.close()

    def ExcluirProduto(Produto):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor = c.cursor()
        sql = "DELETE FROM produtos WHERE codigo = %s"
        val = (Produto.codigo)
        cursor.execute(sql, val)
        c.commit()
        c.close()

    def SelecionarUmProduto(Produto):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor = c.cursor()
        result = []
        sql = "SELECT * FROM produtos WHERE codigo = %s"
        val = (Produto.codigo)
        cursor.execute(sql, val)
        for i in cursor.fetchall():
            result.append(i)
        c.commit()
        c.close()
        return result

    def SelecionarProdutos(self):
        c = mysql.connect("localhost", "root", "", "quartoanoinfo")
        cursor = c.cursor()
        sql = "SELECT * FROM produtos"
        cursor.execute(sql)
        numrows = int(cursor.rowcount)

        array = []
        for i in (0, numrows):
            array.append(i)

        c.commit()
        c.close()
        return array
