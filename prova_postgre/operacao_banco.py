import psycopg2
from connection import Connection

#pip install psycopg2

class Operacoes():

    def salvar(self, nome, genero, autor):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """insert into musica (nome, genero, autor) values ('{0}', '{1}','{2}');""".format(nome, genero, autor)
            cursor.execute(insert)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def atualizar(self,id,nome,genero,autor):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()

            atualiza= """UPDATE musica 
                        SET nome = '{0}', genero = '{1}', autor='{2}' 
                        WHERE id={3};""".format(nome,genero,autor,id)
            #print(atualiza)
            cursor.execute(atualiza)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    def deletar(self,id):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            deleta="delete from musica where id={0}".format(id)
            cursor.execute(deleta)
            connection.commit()
            self.listar()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def listar(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            select = "select * from musica"
            cursor.execute(select)
            pessoas = cursor.fetchall()

            for row in pessoas:
                print("Id = ", row[0], )
                print("nome = ", row[1])
                print("autor  = ", row[2])
                print("genero = ", row[3], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()