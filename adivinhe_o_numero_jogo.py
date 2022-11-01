import sys
import random
import jogos


def divisoria():
    print('\n---', end='\n\n')


def selecionar_novo_jogo():
    print('(1) Jogar Novamente')
    print('(2) Selecionar um Novo Jogo')
    print('(3) Sair', end='\n\n')
    selecionar_novo_jogo_usuario = int(input('Deseja jogar novamente ou selecionar um novo jogo? '))
    if selecionar_novo_jogo_usuario == 1:
        jogar()
        sys.exit()
    elif selecionar_novo_jogo_usuario == 2:
        jogos.selecionar_jogo()
        sys.exit()
    elif selecionar_novo_jogo_usuario == 3:
        print('\nTudo bem, até logo!')
        sys.exit()
    else:
        print('\nOpção inválida. Digite uma opção válida para continuar!')
        sys.exit()




def jogar():
    tentativas = 0
    numero = round(random.randrange(1, 100))

    print('\n------------------------')
    print('-- Adivinhe o número! --')
    print('------------------------', end='\n\n')
    print('(1) Fácil')
    print('(2) Médio')
    print('(3) Difícil', end="\n\n")
    dificuldade_usuario = int(input('Selecione a dificuldade: '))

    if dificuldade_usuario == 1:
        tentativas = 10
    elif dificuldade_usuario == 2:
        tentativas = 5
    elif dificuldade_usuario == 3:
        tentativas = 3
    else:
        print('\nDificuldade inválida. Selecione uma dificuldade válida para continuar!')
        sys.exit()

    for tentativa in range(1, (tentativas + 1)):
        divisoria()
        print(f'Tentativa {tentativa} de {tentativas}.', end='\n\n')
        numero_usuario = int(input('Digite um número: '))
        if numero_usuario < 0 or numero_usuario > 100:
            print('\nNúmero inválido. Digite somente números entre 0 e 100 para jogar!')
            sys.exit()
        elif numero_usuario < numero:
            print('\nMuito baixo...')
            continue
        elif numero_usuario == numero:
            print('\n-----------------------------')
            print('-- Parabéns, você acertou! --')
            print('-----------------------------', end="\n\n")
            selecionar_novo_jogo()
        else:
            print('\nMuito alto...')
            continue

    divisoria()
    print(f'Que pena, o número era {numero}!', end='\n\n')
    selecionar_novo_jogo()


if __name__ == '__main__':
    jogar()
