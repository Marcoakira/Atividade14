from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()

# insert manual de dados na Tabela de Funcionario no banco de dados
def funcionario():

    nome = input("Digite o nome do Funcionarios: ")
    telefone = input("Digite o telefone do Funcionarios: ")
    print("\n inserindo dados ...")
    return conector.inserir(f'''insert into Funcionarios ( nome_func, telefone_func) values ( '{nome}', {telefone});''')

# opcoes = {"c": inserir_clientes, "f": inserir_funcionario, "p": inserir_produto, "v": inserir_vendas}

