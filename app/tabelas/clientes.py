from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()
# insert manual de dados na Tabela de Clitentes no banco de dados
def cliente():

    nome = input("Digite o nome do clientes: ")
    telefone = input("Digite o telefone do Clientes: ")
    print("\n inserindo dados ...")
    return conector.inserir(f'''insert into Clientes ( nome_cliente, telefone_cliente) values ( '{nome}', {telefone});''')