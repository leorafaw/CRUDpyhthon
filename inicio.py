import tkinter as tk
from tkinter import *
from Mysql.Cliente import *
from Mysql.Produto import *

def CadastrarCliente():
    def cadastrarCli():
        nomeA = nome.get()
        cpfA = cpf.get()
        emailA = email.get()
        telefoneA = telefone.get()

        cliente = Cliente(nomeA, cpfA, emailA, telefoneA)
        Cliente.CadastrarCliente(cliente)
        nome.delete(0, 'end')
        cpf.delete(0, 'end')
        email.delete(0, 'end')
        telefone.delete(0, 'end')

    janela = tk.Tk()
    janela.title("CADASTRO DE CLIENTES")
    janela["bg"] = "yellow"
    janela.geometry("260x300")

    tx = Label(janela, text="Nome:", font=("Arial", 10), bg="yellow")
    tx.place(x=8, y=40)
    nome = Entry(janela, width=40)
    nome.place(x=7, y=60)

    tx2 = Label(janela, text="CPF:", font=("Arial", 10), bg="yellow")
    tx2.place(x=8, y=90)
    cpf = Entry(janela, width=40)
    cpf.place(x=7, y=120)

    tx3 = Label(janela, text="Email:", font=("Arial", 10), bg="yellow")
    tx3.place(x=8, y=150)
    email = Entry(janela, width=40)
    email.place(x=7, y=170)

    tx4 = Label(janela, text="Telefone: ", font=("Arial", 10), bg="yellow")
    tx4.place(x=8, y=200)
    telefone = Entry(janela, width=40)
    telefone.place(x=7, y=220)

    btCadastrar = Button(janela, width=10, text="Cadastrar", bg="green", command=cadastrarCli)
    btCadastrar.place(x=90, y=260)

    janela.mainloop()

def CadastrarProduto():
    def cadastrarPro():
        codigoA = codigo.get()
        descriA = descri.get()
        unidadeA = unidade.get()
        prcCompraA = prcCompra.get()
        prcVisA = prcVis.get()

        produto = Produto(codigoA, descriA, unidadeA, prcCompraA, prcVisA)
        Produto.CadastrarProduto(produto)
        codigo.delete(0, 'end')
        descri.delete(0, 'end')
        unidade.delete(0, 'end')
        prcCompra.delete(0, 'end')
        prcVis.delete(0, 'end')

    janela = tk.Tk()
    janela.title("CADASTRO DE PRODUTOS")
    janela["bg"] = "yellow"
    janela.geometry("260x350")

    tx = Label(janela, text="Codigo:", font=("Arial", 10), bg="yellow")
    tx.place(x=8, y=40)
    codigo = Entry(janela, width=40)
    codigo.place(x=7, y=60)

    tx2 = Label(janela, text="Descrição:", font=("Arial", 10), bg="yellow")
    tx2.place(x=8, y=90)
    descri = Entry(janela, width=40)
    descri.place(x=7, y=120)

    tx3 = Label(janela, text="Unidade de Medida:", font=("Arial", 10), bg="yellow")
    tx3.place(x=8, y=150)
    unidade = Entry(janela, width=40)
    unidade.place(x=7, y=170)

    tx4 = Label(janela, text="Preço de Compra: ", font=("Arial", 10), bg="yellow")
    tx4.place(x=8, y=200)
    prcCompra = Entry(janela, width=40)
    prcCompra.place(x=7, y=220)

    tx4 = Label(janela, text="Preço a Vista: ", font=("Arial", 10), bg="yellow")
    tx4.place(x=8, y=250)
    prcVis = Entry(janela, width=40)
    prcVis.place(x=7, y=270)

    btCadastrar = Button(janela, width=10, text="Cadastrar", bg="green", command=cadastrarPro)
    btCadastrar.place(x=90, y=300)

    janela.mainloop()

def VisualizarProdutos():
    def consultarProd():
        codigoA = int(etCodigo.get())
        produto = Produto(codigoA, "", "", 0, 0)
        result = Produto.SelecionarUmProduto(produto)[0]
        txtDesc["text"] = result[2]
        txtUM["text"] = result[3]
        txtPC["text"] = result[4]
        txtPA["text"] = result[5]
    janela = tk.Tk()
    janela.title("CONSULTAR PRODUTOS")
    janela["bg"] = "yellow"
    janela.geometry("260x350")

    txtTitulo = Label(janela, text="Digite o código do produto", font=("Arial", 10), bg="yellow")
    txtTitulo.pack()

    etCodigo = Entry(janela)
    etCodigo.pack()

    btnConsultar = Button(janela, width=5, text="-O", bg="green", command=consultarProd)
    btnConsultar.place(x=200, y=16)

    txtTitDesc = Label(janela, text="Descrição: ", font=("Arial", 10), bg="yellow")
    txtTitDesc.place(x=10, y=50)

    txtDesc = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtDesc.place(x=10, y=70)

    txtTitUM = Label(janela, text="Unidade de Medida:", font=("Arial", 10), bg="yellow")
    txtTitUM.place(x=10, y=90)

    txtUM = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtUM.place(x=10, y=110)

    txtTitPC = Label(janela, text="Preço de Compra:", font=("Arial", 10), bg="yellow")
    txtTitPC.place(x=10, y=130)

    txtPC = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtPC.place(x=10, y=150)

    txtTitPA = Label(janela, text="Preço a Vista:", font=("Arial", 10), bg="yellow")
    txtTitPA.place(x=10, y=170)

    txtPA = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtPA.place(x=10, y=190)

    janela.mainloop()

def VisualizarClientes():
    def consultarCli():
        cpfA = int(etCPF.get())
        cliente = Cliente("", cpfA, "", "")
        result = Cliente.SelecionarUmCliente(cliente)[0]
        txtNome["text"] = result[1]
        txtCPF["text"] = result[2]
        txtEmail["text"] = result[3]
        txtTel["text"] = result[4]
    janela = tk.Tk()
    janela.title("CONSULTAR CLIENTES")
    janela["bg"] = "yellow"
    janela.geometry("260x350")

    txtTitulo = Label(janela, text="Digite o cpf do cliente", font=("Arial", 10), bg="yellow")
    txtTitulo.pack()

    etCPF = Entry(janela)
    etCPF.pack()

    btnConsultar = Button(janela, width=5, text="-O", bg="green", command=consultarCli)
    btnConsultar.place(x=200, y=16)

    txtTitNome = Label(janela, text="Nome: ", font=("Arial", 10), bg="yellow")
    txtTitNome.place(x=10, y=50)

    txtNome = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtNome.place(x=10, y=70)

    txtTitCPF = Label(janela, text="CPF:", font=("Arial", 10), bg="yellow")
    txtTitCPF.place(x=10, y=90)

    txtCPF = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtCPF.place(x=10, y=110)

    txtTitEmail= Label(janela, text="Email:", font=("Arial", 10), bg="yellow")
    txtTitEmail.place(x=10, y=130)

    txtEmail = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtEmail.place(x=10, y=150)

    txtTitTel = Label(janela, text="Telefone:", font=("Arial", 10), bg="yellow")
    txtTitTel.place(x=10, y=170)

    txtTel = Label(janela, text="", font=("Arial", 10), bg="yellow")
    txtTel.place(x=10, y=190)

    janela.mainloop()

def EditaProdutos():
    def editarPro():
        a=""
    def consultarProd():
        codigoB = int(codigo.get())

        produto = Produto(codigoB, "", "", 0, 0)
        Produto.SelecionarUmProduto(produto)

        tx2.place(x=8, y=100)
        descri.place(x=7, y=130)
        tx3.place(x=8, y=160)
        unidade.place(x=7, y=180)
        tx4.place(x=8, y=210)
        prcCompra.place(x=7, y=230)
        tx5.place(x=8, y=260)
        prcVis.place(x=7, y=280)
        btEditar.place(x=90, y=310)

    janela = tk.Tk()
    janela.title("CADASTRO DE PRODUTOS")
    janela["bg"] = "yellow"
    janela.geometry("260x350")

    tx = Label(janela, text="Digite o codigo do produto que deseja editar", font=("Arial", 10), bg="yellow")
    tx.pack()
    codigo=Entry(janela)
    codigo.pack()
    btnConsultar = Button(janela, width=5, text="-O", bg="green", command=consultarProd)
    btnConsultar.place(x=200, y=16)

    tx2 = Label(janela, text="Descrição:", font=("Arial", 10), bg="yellow")
    descri = Entry(janela, width=40)
    tx3 = Label(janela, text="Unidade de Medida:", font=("Arial", 10), bg="yellow")
    unidade = Entry(janela, width=40)
    tx4 = Label(janela, text="Preço de Compra: ", font=("Arial", 10), bg="yellow")
    prcCompra = Entry(janela, width=40)
    tx5 = Label(janela, text="Preço a Vista: ", font=("Arial", 10), bg="yellow")
    prcVis = Entry(janela, width=40)
    btEditar = Button(janela, width=10, text="Editar", bg="green", command=editarPro)

    janela.mainloop()

def EditaClientes():
    a=""

def DelProdutos():
    a=""

def DelClientes():
    a=""

janela = tk.Tk()
janela.title("TELA INICIAL")
janela["bg"] = "white"
janela.geometry("315x500")

txtTitulo = Label(janela,  text="CRUD", font=("Arial", 15), bg="white")
txtTitulo.pack()

btProdutos = Button(janela, width=15, height=5, text="Consultar Produtos", bg="black", fg="white", font=("Arial", 12), command=VisualizarProdutos)
btProdutos.place(x=10, y=50)

btClientes = Button(janela, width=15, height=5, text="Consultar Clientes", bg="black", fg="white", font=("Arial", 12), command=VisualizarClientes)
btClientes.place(x=160, y=50)

btCadPro = Button(janela, width=15, height=5, text="Cadastrar Produtos", bg="black", fg="white", font=("Arial", 12), command=CadastrarProduto)
btCadPro.place(x=10, y=160)

btCadCli = Button(janela, width=15, height=5, text="Cadastrar Clientes", bg="black", fg="white", font=("Arial", 12), command=CadastrarCliente)
btCadCli.place(x=160, y=160)

btEdiPro = Button(janela, width=15, height=5, text="Editar Produtos", bg="black", fg="white", font=("Arial", 12), command=EditaProdutos)
btEdiPro.place(x=10, y=270)

btEdiCli = Button(janela, width=15, height=5, text="Editar Clientes", bg="black", fg="white", font=("Arial", 12), command=EditaClientes)
btEdiCli.place(x=160, y=270)

btDelPro = Button(janela, width=15, height=5, text="Deletar Produtos", bg="black", fg="white", font=("Arial", 12), command=DelProdutos)
btDelPro.place(x=10, y=380)

btDelCli = Button(janela, width=15, height=5, text="Deletar Clientes", bg="black", fg="white", font=("Arial", 12), command=DelClientes)
btDelCli.place(x=160, y=380)

janela.mainloop()