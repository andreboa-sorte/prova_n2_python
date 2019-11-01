from musica import Musicas


musica = Musicas()

menu=True

while menu:
    op=int(input("1- cadastrar\n"
                 "2- alterar\n"
                 "3- deletar\n"
                 "4- ler\n"
                 "5- sair\n"
                 "opção: "))

    if op==1:

        nome = input("digite o da musica: ")
        autor = input("digite o autor da musica - {0} - : ".format(nome))
        genero = input("digite o genero da musica - {0} - : ".format(nome))

        musica.save(nome,autor,genero)

    elif op==2:

        procura=input("digite o nome da musica que se deseja atualizar: ")
        nome = input("digite o nome do aluno: ")
        autor = input("digite o autor da musica - {0} - : ".format(nome))
        genero = input("digite o genero da musica - {0} - : ".format(nome))

        musica.att(procura, nome, autor, genero)

    elif op==3:
        find = input("digite o nome da musica que es deseja deletar: ")

        musica.deleta(find)

    elif op==4:
        acha=input("digite o nome da musica que se deja ver: ")
        musica.ler(acha)

    elif op==5:
        menu=False