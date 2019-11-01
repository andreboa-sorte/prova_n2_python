from pymongo import MongoClient
#pip install pymongo

class MongoConnect():

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.prova  # nome do banco
        self.musica = self.banco.musica  # nome da coleção


    def save(self, json):
        try:
            self.musica.insert_one(json)
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)


    def ler (self, query=None, projection=None):

        for pessoa in self.musica.find(query, projection):
            print(pessoa)


    def att(self, query,field):
        try:
            self.musica.update(query, field)

        except Exception as e:
            print("problema ao atualizar o registro")
            print(json)
            print(e)


    def deleta(self, query):
        try:
            self.musica.remove(query)
        except Exception as e:
            print("problema ao deletar o registro")
            print(query)
            print(e)


