"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,
no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

from random import randint


def jogarDados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1 + dado2


# separar se craps, natural ou ponto se for ponto, jogar novamente até sair 7 ou o ponto
def main():
    resultado = jogarDados()
    if resultado == 7 or resultado == 11:
        print("Natural, você ganhou!")
    elif resultado == 2 or resultado == 3 or resultado == 12:
        print("Craps, você perdeu!")
    else:
        ponto = resultado
        print("Ponto, você precisa tirar", ponto, "novamente")
        while True:
            resultado = jogarDados()
            print("Você tirou", resultado)
            if resultado == ponto:
                print("Você ganhou!")
                break
            elif resultado == 7:
                print("Você perdeu!")
                break


if __name__ == "__main__":
    main()
