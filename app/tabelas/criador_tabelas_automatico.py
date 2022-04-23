from app.connector_and_menu.postgress import Conector_postgres


class Criador_tabelas_automatico(Conector_postgres):
    def __init__(self):
        self.self = self
        self.conector = Conector_postgres()
        super().__init__()

    def tabela_produtos(self):
        self.conector.inserir(f''' create table if not exists Produtos (
                                    id_produto serial,
                                    nome_produto VARCHAR(50),
                                    qtde_estoque INT,
                                    CONSTRAINT produtos_pk PRIMARY KEY (id_produto)
                                ); ''')

    def tabela_clientes(self):
        self.conector.inserir(f''' create table if not exists Clientes (
                                    id_cliente serial,
                                    nome_cliente VARCHAR(50),
                                    telefone_cliente VARCHAR(50),
                                    CONSTRAINT clientes_pk PRIMARY KEY (id_cliente)
                                ); ''')

    def tabela_funcionarios(self):
        self.conector.inserir(f''' create table if not exists Funcionarios (
                                    id_func serial,
                                    nome_func VARCHAR(50),
                                    telefone_func VARCHAR(50),
                                    CONSTRAINT funcionarios_pk PRIMARY KEY (id_func)
                                ); ''')

    def tabela_vendas(self):
        self.conector.inserir(f''' create table IF NOT EXISTS Vendas (
                                    id_venda serial,
                                    id_produto INT,
                                    qtde_venda INT,
                                    id_func INT,
                                    id_cliente INT,
                                    CONSTRAINT vendas_pk PRIMARY KEY (id_venda),
                                    CONSTRAINT vendas_fk FOREIGN KEY (id_produto) REFERENCES Produtos (id_produto),
                                    CONSTRAINT vendas_fk2 FOREIGN KEY (id_func) REFERENCES Funcionarios (id_func),
                                    CONSTRAINT vendas_fk3 FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
                                ); ''')

    # cria a tabela log de vendas automaticamente e insere os dados atraves do metodo trigger de inserção e gatilho de atualização
    def tabela_log(self):
        self.conector.inserir(f''' CREATE TABLE IF NOT EXISTS vendas_log(
                                    id_log serial,
                                    id_func integer,
                                    data_venda timestamp
                                );
                                                                
                               CREATE OR REPLACE FUNCTION VENDAS_GATILHO()
                                    RETURNS TRIGGER AS $VENDAS_GATILHO$
                                        BEGIN
                                            IF(TG_OP = 'INSERT') THEN
                                                INSERT INTO vendas_log (id_func, data_venda) VALUES
                                                    ('Venda realizada pelo id ' || new.id_func, 'Venda realizada em ' || current_timestamp);
                                                RETURN NEW;
                                            END IF;
                                        END;
                                    $VENDAS_GATILHO$
                                    LANGUAGE plpgsql;
                                
                                CREATE TRIGGER VENDAS_GATILHO BEFORE INSERT ON VENDAS
                                FOR EACH ROW EXECUTE PROCEDURE VENDAS_GATILHO(); ''')


def criador_all():
    criador = Criador_tabelas_automatico()
    criador.tabela_produtos()
    criador.tabela_clientes()
    criador.tabela_funcionarios()
    criador.tabela_vendas()
    criador.tabela_log()
