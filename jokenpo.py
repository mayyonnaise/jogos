import random

sair = False

while not sair:
    print('Bora jogar?')    
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    print('4 - sair')
    print('Escolha uma opção: ')
    opcao = int(input(""))
    escolha_pc = random.randint(1, 3)




    if (opcao == 1): 
        if (escolha_pc == 1):
            print("pc escolheu pedra, empate.")

        elif (escolha_pc == 2):
            print("pc escolheu papel, você perdeu.") 
        elif (escolha_pc == 3):
            print ("pc escolheu tesoura, você ganhou.")
    elif (opcao == 2): 
        if (escolha_pc == 1):
            print("pc escolheu pedra, você perdeu.")
        elif (escolha_pc == 2):
            print("o pc escolheu papel, empate.")
        elif (escolha_pc == 3):
            print("pc escolheu tesoura, você perdeu.")
    elif (opcao == 3): 
        if (escolha_pc == 1):
            print("pc escolheu pedra, você perdeu.")
        elif (escolha_pc == 2):
            print("pc escolheu papel, você ganhou.")
        elif (escolha_pc == 3):
            print("pc escolheu tesoura, empate.")
    else: 
        sair = True
        print("jogo encerrado, até a próxima")
