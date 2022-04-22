from app.tabelas.criador_de_tabelas import criar

# Menu principal
def criar_tabela():
    criar()
def inserir_dados():
    criar()

def exibir_dados():
        criar()

def sair():
    print("Obrigado por usar o sistema")
    exit()



my_menu = {"C": criar_tabela,
           "I": inserir_dados,
           "E": exibir_dados,
           "S": sair}



escolher_opcao = input("Oque deseja fazer? Digite a Inicial (\033[1;31m C\033[mriar uma tabela\n\033[1;31m I\033[mnserir dados a uma tabela existente \033[1;31m\nE\033[mxibir relatorio (log)\033[1;31m").upper()

my_menu[escolher_opcao]()



class Menu_principal:

    def __init__(self, ):
        pass

    # Menu principal
    def criar_tabela(self):
        criar()

    def inserir_dados(self):
        criar()

    def exibir_dados(self):
        criar()

    def sair(self):
        print("Obrigado por usar o sistema")
        exit()
    def menu(self):
        my_menu = {"C": criar_tabela,
                   "I": inserir_dados,
                   "E": exibir_dados,
                   "S": sair}

        escolher_opcao = input(
            "Oque deseja fazer? Digite a Inicial (\033[1;31m C\033[mriar uma tabela\n\033[1;31m I\033[nserir dados a uma tabela existente \033[1;31m\nE\033[mxibir relatorio (log)\033[1;31m").upper()

        my_menu[escolher_opcao]()




if __name__ == "__main__":
    Menu_principal().menu()