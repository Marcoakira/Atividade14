from app.connector_and_menu.postgress import Conector_postgres


class Criar_tabela(Conector_postgres):
    def __init__(self):
        self.self = self
        self.conector = Conector_postgres()
        super().__init__()

    def criar_tabela_nova(self):
        nome_da_tabela = input("Digite o nome da tabela: ")
        colunas = input("Digite as colunas e seus tipos separadas por virgula: ex: nome varchar(50), idade int etc: ")
        tem_pk = input("Tem chave primaria? (s/n): ").lower()
        if tem_pk == "s":
            chave_primaria = input("Digite a chave primaria: ")
            tem_fk = input("Tem chave estrangeira? (s/n): ").lower()
            if tem_fk == "s":
                chave_estrangeira = input("Digite o nome da chave estrangeira: ")
                chave_estrangeira_tabela = input("Digite o nome da tabela da chave estrangeira: ")
                chave_estrangeira_referencia = input("Digite a coluna estrangeira de referencia: ")
                return self.conector.inserir(f''' CREATE TABLE IF NOT EXISTS {nome_da_tabela}(
                            {colunas},    
    
                            -- DEFININDO CHAVE PRIMARIA
                            CONSTRAINT {chave_primaria}_pk PRIMARY KEY ({chave_primaria}),
                            -- DEFININDO CHAVE ESTRANGEIRA
                            CONSTRAINT {chave_estrangeira}_fk FOREIGN KEY ({chave_estrangeira}) REFERENCES {chave_estrangeira_tabela} ({chave_estrangeira_referencia})
                         );''')
            else:

                return self.conector.inserir(f''' CREATE TABLE IF NOT EXISTS {nome_da_tabela}(
                {colunas},    
                    
                -- DEFININDO CHAVE PRIMARIA
                CONSTRAINT {chave_primaria}_pk PRIMARY KEY ({chave_primaria})
                
             );''')

        else:
            return self.conector.inserir(f''' CREATE TABLE IF NOT EXISTS {nome_da_tabela}(
                {colunas}
             );''')

def criar():
    criar_tabela = Criar_tabela()
    criar_tabela.criar_tabela_nova()