from pymongo import MongoClient

from conexao import MongoConnect

class Musicas():

    conexao = None

    def __init__(self):
        self.conexao = MongoConnect()

    def save(self, nome, autor, genero):

        aluno = {'nome': nome, 'autor': autor, 'genero': genero}
        self.conexao.save(aluno)

    def att(self, procura, nome, autor, genero):
        musica = {'nome': nome, 'autor': autor, 'genero': genero}
        self.conexao.att({"nome": procura}, {"$set": musica})

    def deleta(self, find):
        self.conexao.deleta({"nome": find})

    def ler(self, acha):
        self.conexao.ler({"nome":acha},{"_id":0})


