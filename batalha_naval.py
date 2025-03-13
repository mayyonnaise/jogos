oceano = [
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,3,2,0,0,0],
    [0,3,2,0,4,4],
    [0,3,0,0,4,4],
    [0,0,0,0,0,0]
]

# 1 = navio C
# 2 = navio D
# 3 = navio A
# 4 = navio B

navioC = 1
navioD = 2
navioA = 3
navioB = 4

print("jogo naval")

sair = False

while (not sair):
    print("o oceano tem 6 linhas (de 1 a 6) e 6 colunas (de 1 a 6)")
    print("exemplo de opcao: 23 (significa linha 2 coluna 3)")
    opcao = input(("escolha uma opcao: "))
    linha = int(opcao[0])-1
    coluna = int(opcao[1])-1
    verificacao = int(opcao)
    print(linha)
    print(coluna)
    if (verificacao >= 11 and verificacao <= 66):
        if (oceano[linha][coluna] == 1):
            print("parabens, voce eliminou o navio C")
            navioC -= 1
            print("Esse navio ainda tem {} unidades.".format(navioC))
            oceano[linha][coluna] = 0
        elif (oceano[linha][coluna] == 3):
            print("parabens, voce acertou o navio A")
            navioA -= 1
            print("Esse navio ainda tem {} unidades.".format(navioA))
            oceano[linha][coluna] = 0
        elif (oceano[linha][coluna] == 2):
            print("parabens, voce acertou o navio D")
            navioD -= 1
            print("Esse navio ainda tem {} unidades.".format(navioD))
            oceano[linha][coluna] = 0
        elif (oceano[linha][coluna] == 4):
            print("parabens, voce acertou o navio B")
            navioB -= 1
            print("Esse navio ainda tem {} unidades.".format(navioB))
            oceano[linha][coluna] = 0
        else:
            print("opcao incorreta")
    else:
        print("essa regiao do oceano nao existe")

    print("deseja continuar? 1 - sim // 2 - nao")
    opcao2 = int(input())
    if (opcao2 != 1):
        sair = True
    
