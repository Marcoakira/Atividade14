from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()

def produto():
    nome = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade do produto no estoque: ")
    print("\n inserindo dados ...")
    return conector.inserir(f'''insert into produtos ( nome_produto, qtde_estoque) values ( '{nome}', {quantidade});''')












