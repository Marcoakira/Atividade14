from app.tabelas.produtos import produto
from app.tabelas.clientes import cliente
from app.tabelas.funcionarios import funcionario
from app.tabelas.vendas import venda



def menu_inserir():
  escolha = input("\n\n\033[1;34m P\033[mrodutos \n\033[1;34m C\033[mlientes \n\033[1;34m F\033[muncionarios \n\033[1;3"
                  "4m V\033[mendas \n\033[1;34mInserir dados Menualmente em qual tabela ? : \033[m").upper()
  if escolha == "P":
    produto() # chama a função produto
  elif escolha == "C":
    cliente()   # chama a função cliente
  elif escolha == "F":
    funcionario() # chama a função funcionario
  elif escolha == "V":
    venda() # chama a função venda

