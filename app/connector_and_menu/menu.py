from app.tabelas.criador_de_tabelas import criar
from app.tabelas.criador_tabelas_automatico import criador_all
from app.tabelas.menu_inserir_dados import menu_inserir

class Menu_principal:

    def __init__(self, ):
        pass

    # Menu principal
    def criar_tabela(self):
        criar()

    def criar_todas_tabela(self):
        criador_all()

    def inserir_dados(self):
        menu_inserir()

    def trigger_function(self):
        criar()

    def exibir_dados(self):
        criar()

    def sair(self):
        print("Obrigado por usar o sistema")
        exit()
    def menu(self):
        my_menu = {"C": self.criar_tabela,
                   "F": self.criar_todas_tabela,
                   "I": self.inserir_dados,
                   "M": self.trigger_function,
                   "E": self.exibir_dados,
                   "S": self.sair}

        escolher_opcao = input(
            " \n\033[1;31m C\033[mriar uma tabela\n\033[1;31m F\033[mazer automaticamente as tabelas(produtos, clientes, funcionários, vendas e log)\n\033[1;31m I\033[mnserir dados a uma tabela existente \033[1;31m \n\033[1;31m M\033[montar automaticamente uma Trigger Function que alimente uma tabela de log \033[1;31m \n E\033[mxibir relatorio (log)\033[1;31m \n S\033[mair\033[1;31m \n\nOque deseja fazer? Digite a Inicial: \033[m").upper()

        my_menu[escolher_opcao]()




if __name__ == "__main__":
    Menu_principal().menu()