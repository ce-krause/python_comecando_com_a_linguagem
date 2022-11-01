import adivinhe_o_numero_jogo
import forca_jogo


def selecionar_jogo():
    print('\n------------')
    print('-- Jogos! --')
    print('------------', end='\n\n')
    print('(1) Adivinhe o número!')
    print('(2) Forca!', end='\n\n')
    selecionar_jogo_usuario = int(input('Selecione o jogo: '))

    if selecionar_jogo_usuario == 1:
        adivinhe_o_numero_jogo.jogar()
    elif selecionar_jogo_usuario == 2:
        forca_jogo.jogar()


if __name__ == '__main__':
    selecionar_jogo()
