from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()

# insert manual de dados na Tabela de produtos no banco de dados
def venda():

    id_produto = input("Digite o id do produto: ")
    quantidade = input("Digite a quantidade do produto vendida: ")
    id_funcionario = input("Digite o id do funcionario: ")
    id_cliente = input("Digite o id do cliente: ")
    print("\n inserindo dados ...")
    return conector.inserir(f'''insert into vendas (id_produto, qtde_venda, id_func, id_cliente) values ( {id_produto },{quantidade }, {id_funcionario},{id_cliente} );''')
