from operacao_banco import Operacoes

op = Operacoes()

menu=True
while menu:
    aux=int(input("1- cadastrar\n"
                  "2- atualizar\n"
                  "3- listar\n"
                  "4- deletar\n"
                  "5- sair\n"
                  "opção: "))

    if aux==1:

        nome = str(input("Digite o nome da musica: "))
        genero = str(input("Digite o genero da musica - {0} -: ".format(nome)))
        autor=str(input("digite o autor da musica - {0} - : ".format(nome)))
        op.salvar(nome,genero,autor)

    elif aux==2:

        id=int(input("digite o o ID do cadastro a ser atualizado: "))

        nome=str(input("digite novo nome da musica: "))
        genero=str(input("digite o novo genero da musica: "))
        autor=str(input("digite o novo autor da musica: "))

        op.atualizar(id,nome,genero,autor)


    elif aux == 3:
        op.listar()

    elif aux==4:
        id=int(input("digite o ID do registro a ser deletado: "))
        op.deletar(id)

    elif aux==5:
        menu=False
