from random import randrange
from click import clear

def exibir_tabuleiro(tabuleiro):
    clear()
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def fazer_jogada(tabuleiro):
    ok = False
    while not ok:
        movimento = input("Digite seu movimento (1-9): ")
        ok = len(movimento) == 1 and movimento.isdigit() and '1' <= movimento <= '9'
        if ok:
            movimento = int(movimento) - 1
            linha, coluna = movimento // 3, movimento % 3
            ok = tabuleiro[linha][coluna] not in ['O', 'X']
            if ok:
                tabuleiro[linha][coluna] = 'O'
            else:
                print("Campo já ocupado - repita sua entrada!")
                ok = False
        else:
            print("Movimento inválido - repita sua entrada!")

def listar_campos_livres(tabuleiro):
    livres = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] not in ['O', 'X']]
    return livres

def verificar_vitoria(tabuleiro, simbolo):
    diagonal1 = diagonal2 = True
    for rc in range(3):
        if all(tabuleiro[rc][col] == simbolo for col in range(3)):
            return 'computador' if simbolo == 'X' else 'jogador'
        if all(tabuleiro[linha][rc] == simbolo for linha in range(3)):
            return 'computador' if simbolo == 'X' else 'jogador'
        if tabuleiro[rc][rc] != simbolo:
            diagonal1 = False
        if tabuleiro[rc][2 - rc] != simbolo:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return 'computador' if simbolo == 'X' else 'jogador'
    return None

def jogada_computador(tabuleiro):
    livres = listar_campos_livres(tabuleiro)
    if livres:
        linha, coluna = livres[randrange(len(livres))]
        tabuleiro[linha][coluna] = 'X'

# Inicialização do jogo
tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'

vez_do_jogador = True
vencedor = None

while listar_campos_livres(tabuleiro):
    exibir_tabuleiro(tabuleiro)
    if vez_do_jogador:
        fazer_jogada(tabuleiro)
    else:
        jogada_computador(tabuleiro)
    vencedor = verificar_vitoria(tabuleiro, 'O' if vez_do_jogador else 'X')
    if vencedor:
        break
    vez_do_jogador = not vez_do_jogador

exibir_tabuleiro(tabuleiro)

if vencedor == 'jogador':
    print("Você ganhou!")
elif vencedor == 'computador':
    print("Eu venci!")
else:
    print("Empate!")
