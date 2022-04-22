from app.connector_and_menu.postgress import Conector_postgres

conector = Conector_postgres()



def inserir_produto():

    nome = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade do produto no estoque: ")
    return conector.inserir(f'''insert into teste ( nome_produto, qtde_estoque) values ( '{nome}', {quantidade});''')

def inserir_clientes():

    nome = input("Digite o nome do clientes: ")
    telefone = input("Digite o telefone do Clientes: ")
    return conector.inserir(f'''insert into Clientes ( nome_cliente, telefone_cliente) values ( '{nome}', {telefone});''')

def inserir_funcionario():

    nome = input("Digite o nome do Funcionarios: ")
    telefone = input("Digite o telefone do Funcionarios: ")
    return conector.inserir(f'''insert into Funcionarios ( nome_func, telefone_func) values ( '{nome}', {telefone});''')

def inserir_vendas():

    id_produto = input("Digite o id do produto: ")
    quantidade = input("Digite a quantidade do produto vendida: ")
    id_funcionario = input("Digite o id do funcionario: ")
    id_cliente = input("Digite o id do cliente: ")

    return conector.inserir(f'''insert into clietes (id_produto, qtde_venda, id_func, id_cliente) values ( {id_produto },{quantidade }, {id_funcionario},{id_cliente} );''')

opcoes = {"c": inserir_clientes, "f": inserir_funcionario, "p": inserir_produto, "v": inserir_vendas}


def inicio():

    escolha =input("Qual tabela deseja criar? , c/f/p/v: ")

    oquefazer = opcoes[escolha]
    oquefazer()



inicio()











# TODO: Terminar de criar o criador de tabelas

#     def criar_tabela_cliente(self):
#         self.campo1 = ''campo1''
#
#
#
#     return inserir('''create table teste (
# 	campo1 varchar(50)
# 	nome VARCHAR(50),
# 	preco DECIMAL(5,2),
# 	estoque INT
# );''')
#
# batata = CriaTabelas()
# batata.inserir('''create table Produtos (
# 	id_produto serial,
# 	nome_produto VARCHAR(50),
# 	qtde_estoque INT,
# 	CONSTRAINT produtos_pk PRIMARY KEY (id_produto)
# );''')