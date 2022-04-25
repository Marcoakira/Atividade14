from app.connector_and_menu.postgress import Conector_postgres

conector = Conector_postgres()


# criar triggers para a tabela vendas e log,
# e outro para que seja possivel atualizar a tabela produtos com a quantidade de estoque
def trigger_log():
    return conector.inserir(''' 	CREATE OR REPLACE FUNCTION VENDAS_GATILHO()
                                        RETURNS TRIGGER AS $VENDAS_GATILHO$
                                            BEGIN
                                                IF(TG_OP = 'INSERT') THEN
                                                    INSERT INTO vendas_log (id_func, data_venda) VALUES
                                                        ( new.id_func, current_timestamp);
                                                    RETURN NEW;
                                                END IF;
                                            END;
                                        $VENDAS_GATILHO$
                                        LANGUAGE plpgsql; ''')


def trigger_estoque():
    return conector.inserir('''CREATE TRIGGER Tgr_vendas_insert AFTER INSERT
                                        ON vendas     FOR EACH ROW
                                        BEGIN
                                            UPDATE Produtos SET qtde_estoque = qtde_estoque + NEW.qtde_venda 
                                        WHERE id_produto = NEW.Produto;
                                        END$
                                         
                                        CREATE TRIGGER Tgr_vendas_Delete AFTER DELETE
                                        ON vendas
                                        FOR EACH ROW
                                        BEGIN
                                            UPDATE Produtos SET qtde_estoque = qtde_estoque - OLD.qtde_venda
                                        WHERE id_produto = OLD.Produto;
                                        SHOW triggers;
                                        END$''')


def criar_triggers():
    trigger_log()
    trigger_estoque()
