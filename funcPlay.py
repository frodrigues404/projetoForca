
from funcMid import *
from format import *

def play():
    clear()
    print('===' * 10)
    player1 = str(input('Digite o nome do jogador 1: ')).strip().capitalize()
    player2 = str(input('Digite o nome do jogador 2: ')).strip().capitalize()
    print('-' * 10)
    palavraSecreta = str(input(f'{player1}, Digite a palavra secreta: ')).lower().strip()
    letrasDescobertas = []
    print('-' * 10)
    try:
        dica1 = str(input('Digite a primeira dica: ')).lower().strip()
        dica2 = str(input('Digite a segunda dica: ')).lower().strip()
        dica3 = str(input('Digite a terceira dica: ')).lower().strip()
    except:
        print('Valor digitado incorretamente.')
    clear()
    print('-' * 10)
    mainFunc(palavraSecreta, letrasDescobertas, player2, dica1, dica2, dica3, player1)
    try:
        jogarNovamente = str(input('Deseja jogar novamente? [S/N]: ')).lower().strip()
    except:
        print('Valor inválido.')
    if jogarNovamente == 'n':
        print('Obrigado por jogar!')
    elif jogarNovamente == 's':
        return play()
