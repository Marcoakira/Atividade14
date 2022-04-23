import pandas as pd
from time import sleep
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
        conector.inserir(f'''insert into produtos ( nome_produto, qtde_estoque) values ( '{row['nome_produto']}', {row['qtde_estoque']});''')


def cad_clientes():
    """
    Função que cadastra os clientes
    """

    cli_files = pd.read_csv("clientes.csv")
    for index, row in cli_files.iterrows():
        conector.inserir(f'''insert into Clientes ( nome_cliente, telefone_cliente) values ( '{row['nome_cliente']}', '{row['telefone_cliente']}');''')


def cad_vendas():
    """
    Função que cadastra as vendas
    """
    vendas_files = pd.read_csv("vendas.csv")
    menor_valor = 0
    maior_valor = 10
    new_table = vendas_files['id_venda'] > menor_valor and vendas_files['id_venda'] < maior_valor
    loop = 0
    quantidade = int(input("quantos testes deseja realizar?"))
    while loop < quantidade:
        for index, row in new_table.iterrows():
            conector.inserir(f'''insert into vendas (id_produto, qtde_venda, id_func, id_cliente) values ( {row['id_produto']},{row['qtde_venda'] }, {row['id_func']},{row['id_cliente']} );''')
            loop += 1
            menor_valor += 10
            maior_valor += 10
            print(f"{loop} testes realizados, total de {maior_valor} dados inseridos, aguarde 1 minuto até o proximo teste...")
            if loop == quantidade:
                print(f"finalizamos os testes")
                break
            sleep(60)

    for index, row in vendas_files.iterrows():
        conector.inserir(f'''insert into Vendas ( id_funcionario, id_produto, id_cliente, data_venda, valor_venda) values ( {row['id_funcionario']}, {row['id_produto']}, {row['id_cliente']}, '{row['data_venda']}', {row['valor_venda']});''')



def geral():
    # escolha = input(" sera iniciada a rotina de testes de vendas, deseja antes inserir a base de Funcionarios,Clientes e Produtos? (s/n)")
    # if escolha == "s":
    #     cad_funcionarios()
    #     cad_produtos()
    #     cad_clientes()
    cad_vendas()