from app.tabelas.criador_de_tabelas import criar
from app.tabelas.criador_tabelas_automatico import criador_all
from app.tabelas.menu_inserir_dados import menu_inserir
from app.tabelas.triggers import criar_triggers
from app.bd.rotina import geral
from app.tabelas.log import print_logs

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
        criar_triggers()

    def exibir_dados(self):
        print_logs()

    def rotina_teste(self):
        geral()

    def sair(self):
        print("Obrigado por usar o sistema")
        exit()
    def menu(self):
        my_menu = {"C": self.criar_tabela,
                   "F": self.criar_todas_tabela,
                   "I": self.inserir_dados,
                   "M": self.trigger_function,
                   "R": self.rotina_teste,
                   "E": self.exibir_dados,
                   "S": self.sair}

        escolher_opcao = input(
            " \n\033[1;31m C\033[mriar uma tabela\n\033[1;31m F\033[mazer automaticamente as tabelas(produtos, clientes,"
            " funcionários, vendas, log) e os ( Triggers )\n\033[1;31m I\033[mnserir dados a uma tabela existente"
            " \033[1;31m \n\033[1;31m M\033[montar automaticamente uma Trigger Function que alimente uma tabela de log "
            "e atualiza qtd em estoque\033[1;31m \n R\033[motina de testes Automatizado \033[1;31m \n E\033[mxibir relatorio (log)\033[1;31m \n S\033[mair\033[1;31m \n\nO"
            "que deseja fazer? Digite a Inicial: \033[m").upper()

        my_menu[escolher_opcao]()




if __name__ == "__main__":
    Menu_principal().menu()