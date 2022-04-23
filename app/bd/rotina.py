import pandas as pd
from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()



def cad_funcionarios():
    """
    Função que cadastra os funcionários
    """
    func_files = pd.read_csv("funcionarios.csv")
    for index, row in func_files.iterrows():
        conector.inserir(f'''insert into Funcionarios ( nome_func, telefone_func) values ( '{row['nome_func']}', {row['telefone_func']});''')


def cad_produtos():
    """
    Função que cadastra os produtos
    """
    prod_files = pd.read_csv("produtos.csv")
    for index, row in prod_files.iterrows():
        conector.inserir(f'''insert into teste ( nome_produto, qtde_estoque) values ( '{row['nome_produto']}', {row['qtde_estoque']});''')

def cad_clientes():
    """
    Função que cadastra os clientes
    """
    func_files = pd.read_csv("funcionarios.csv")
    for index, row in func_files.iterrows():
        conector.inserir(f'''insert into Clientes ( nome_cliente, telefone_cliente) values ( '{row['nome_cliente']}', {row['telefone_cliente']});''')

def cad_vendas():
    """
    Função que cadastra as vendas
    """
    vendas_files = pd.read_csv("vendas.csv")

    for index, row in vendas_files.iterrows():
        conector.inserir(f'''insert into Vendas ( id_funcionario, id_produto, id_cliente, data_venda, valor_venda) values ( {row['id_funcionario']}, {row['id_produto']}, {row['id_cliente']}, '{row['data_venda']}', {row['valor_venda']});''')

def geral():
    escolha = input(" sera iniciada a rotina de testes de vendas, deseja antes inserir a base de Funcionarios,Clientes e Produtos? (s/n)")
    if escolha == "s":
        cad_funcionarios()
        cad_produtos()
        cad_clientes()
    cad_vendas()