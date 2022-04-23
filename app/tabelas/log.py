from app.connector_and_menu.postgress import Conector_postgres
conector = Conector_postgres()
# insert manual de dados na Tabela de Clitentes no banco de dados
def print_logs():
    dados_log = conector.inserir(''' select * from vendas_log; ''')
    print(dados_log)