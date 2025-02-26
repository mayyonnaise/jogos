import random

sair = False

while not sair:
    print('Bora jogar?')    
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    print('4 - Lagarto')
    print('5 - Spock')
    print('6 - sair')
    print('Escolha uma opção: ')
    opcao = int(input(""))
    escolha_pc = random.randint(1, 5)


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
    elif (opcao == 4):
        if (escolha_pc == 1):
            print("pc escolheu pedra, você perdeu.")
        elif (escolha_pc == 2):
            print("pc escolheu papel, você ganhou.")
        elif (escolha_pc == 3):
            print("pc escolheu tesoura, você perdeu.")
        elif (escolha_pc == 4):
            print("pc escolheu lagarto, empate.")
        elif (escolha_pc == 5):
            print("pc escolheu spock, você ganhou.")
    elif (opcao == 5):
        if (escolha_pc == 1):
            print("pc escolheu pedra, você ganhou.")
        elif (escolha_pc == 2):
          print("pc escolheu papel, você perdeu.")
        elif (escolha_pc == 3):
            print("pc escolheu tesoura, você ganhou.")
        elif (escolha_pc == 4):
            print("pc escolheu lagarto, você perdeu.")
        elif (escolha_pc == 5):
            print("pc escolheu spock, empate.")
    else: 
        sair = True
        print("jogo encerrado, até a próxima")