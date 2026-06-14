import random

#Proximos passos:
#mudar carta 1 e carta dois pra usar a bibilhoteca do samu
#Fazer split depois, mas bem depois


dinheiro = 50

#FAZER ISSO FUNCIONAR COM O NOVO VETOR
def dealar(aleatorio:int,valor:int,total:int,carta):
    aleatorio = random.randint(0,51)
    valor = cartas[aleatorio]['valor']

    if (total + valor) > 21 and valor == 11:
        total = valor + total - 10
    else:
        total = valor + total
    return n2


while dinheiro > 0:
    #dicionario de todas as cartas
    cartas = [
    # === ESPADAS (Spades) ===
    {'card': "\U0001F0A1", 'valor': 11},  # Ás
    {'card': "\U0001F0A2", 'valor': 2},   # 2
    {'card': "\U0001F0A3", 'valor': 3},   # 3
    {'card': "\U0001F0A4", 'valor': 4},   # 4
    {'card': "\U0001F0A5", 'valor': 5},   # 5
    {'card': "\U0001F0A6", 'valor': 6},   # 6
    {'card': "\U0001F0A7", 'valor': 7},   # 7
    {'card': "\U0001F0A8", 'valor': 8},   # 8
    {'card': "\U0001F0A9", 'valor': 9},   # 9
    {'card': "\U0001F0AA", 'valor': 10},  # 10
    {'card': "\U0001F0AB", 'valor': 10},  # Valete (J)
    {'card': "\U0001F0AD", 'valor': 10},  # Dama (Q)
    {'card': "\U0001F0AE", 'valor': 10},  # Rei (K)

    # === COPAS (Hearts) ===
    {'card': "\U0001F0B1", 'valor': 11},  # Ás
    {'card': "\U0001F0B2", 'valor': 2},   # 2
    {'card': "\U0001F0B3", 'valor': 3},   # 3
    {'card': "\U0001F0B4", 'valor': 4},   # 4
    {'card': "\U0001F0B5", 'valor': 5},   # 5
    {'card': "\U0001F0B6", 'valor': 6},   # 6
    {'card': "\U0001F0B7", 'valor': 7},   # 7
    {'card': "\U0001F0B8", 'valor': 8},   # 8
    {'card': "\U0001F0B9", 'valor': 9},   # 9
    {'card': "\U0001F0BA", 'valor': 10},  # 10
    {'card': "\U0001F0BB", 'valor': 10},  # Valete (J)
    {'card': "\U0001F0BD", 'valor': 10},  # Dama (Q)
    {'card': "\U0001F0BE", 'valor': 10},  # Rei (K)

    # === OUROS (Diamonds) ===
    {'card': "\U0001F0C1", 'valor': 11},  # Ás
    {'card': "\U0001F0C2", 'valor': 2},   # 2
    {'card': "\U0001F0C3", 'valor': 3},   # 3
    {'card': "\U0001F0C4", 'valor': 4},   # 4
    {'card': "\U0001F0C5", 'valor': 5},   # 5
    {'card': "\U0001F0C6", 'valor': 6},   # 6
    {'card': "\U0001F0C7", 'valor': 7},   # 7
    {'card': "\U0001F0C8", 'valor': 8},   # 8
    {'card': "\U0001F0C9", 'valor': 9},   # 9
    {'card': "\U0001F0CA", 'valor': 10},  # 10
    {'card': "\U0001F0CB", 'valor': 10},  # Valete (J)
    {'card': "\U0001F0CD", 'valor': 10},  # Dama (Q)
    {'card': "\U0001F0CE", 'valor': 10},  # Rei (K)

    # === PAUS (Clubs) ===
    {'card': "\U0001F0D1", 'valor': 11},  # Ás
    {'card': "\U0001F0D2", 'valor': 2},   # 2
    {'card': "\U0001F0D3", 'valor': 3},   # 3
    {'card': "\U0001F0D4", 'valor': 4},   # 4
    {'card': "\U0001F0D5", 'valor': 5},   # 5
    {'card': "\U0001F0D6", 'valor': 6},   # 6
    {'card': "\U0001F0D7", 'valor': 7},   # 7
    {'card': "\U0001F0D8", 'valor': 8},   # 8
    {'card': "\U0001F0D9", 'valor': 9},   # 9
    {'card': "\U0001F0DA", 'valor': 10},  # 10
    {'card': "\U0001F0DB", 'valor': 10},  # Valete (J)
    {'card': "\U0001F0DD", 'valor': 10},  # Dama (Q)
    {'card': "\U0001F0DE", 'valor': 10}   # Rei (K)
]


    #lista de cartas possiveis do 21 (menos o 1, vejo isso depois)
    cartas = list(range(2,12))
    #outras variaveis
    aux = 0
    carta1 = 0
    carta2 = 0
    casa = 0
    start = 0
    ale = 0
    acao = '0'

    #tela de entrada
    print('Bem vindo ao blackjack \U0001F0A1 \U0001F0B1 \U0001F0C1 \U0001F0D1')

    #enter pra iniciar o jogo
    start = input('"ENTER" pra jogar:')
    print(f"Você tem {dinheiro} reais")
    #aposta
    while True:
        aposta = int(input("Quanto vc aposta:"))
        if aposta > dinheiro:
            print("Nao aposte mais do que tem")
        else:
            break


    #mostrar a pontuação da casa com uma carta
    casa = dealar(ale, casa)
    print (f"Casa: {casa}, X")
    #tirar a segunda carta e somar com o total da casa
    start = dealar(ale,casa)
    casa = casa + start

    start = input("--->")

    #mostrar as duas primeiras cartas
    carta1 = dealar(ale,carta1)
    carta2 = dealar(ale,carta2)
    player = carta1 + carta2
    #em caso de balackjack
    if player == 21:
        print(f"VOCE GANHOU COM UM BLACKJACK")
        dinheiro = dinheiro + aposta * 2
        #reiniciar ou terminar o jogo
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break
    print (f"Voce: {carta1},{carta2}, Total: {player}")

    while acao != "":
        #Ação do jogador
        acao = (input("O que fazer: Hit = 1, Double = 2, Hit and Double = 3, nada pra continuar:  "))
        match acao:
            case "1":
                aux = player
                player = dealar(ale,player)
                carta1 = player - aux
                print('voce tirou um ', carta1)
            case "2":
                aposta = aposta * 2
                print("sua aposta agora é: ", aposta)
            case "3":
                aux = player
                player = dealar(ale,player)
                carta1 = player - aux
                print('voce tirou um ', carta1)
                aposta = aposta * 2
                print("sua aposta agora é: ", aposta)

        #mostrar quantos pontos tem por enquanto
        print("seus pontos: ", player)

        #teste pra ver se perdeu
        if player > 21:
            acao = ''

     #teste pra ver se perdeu
    if player > 21:
        print(f"fim de jogo, voce perdeu com {player} pontos.")
        dinheiro = dinheiro - aposta
        #reiniciar ou terminar o jogo
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break



    start = input("--->")
    #revelar pontuação total da casa
    print("vez da casa:")
    print("pontuacao total da casa é: ", casa)
    #caso a casa tire um blackjack
    if casa == 21:
        print("CASA TIROU UM BLACKJACK")
        print("VOCE PERDEU")
        dinheiro = dinheiro - aposta
        #reiniciar ou terminar o jogo
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break

    #ação da casa
    while casa < 17:
        print("Casa hit")

        #RESOLVE CARALHO FDP
        '''
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        QQQQQQQQQQQQQQQQQQQQQ
        UUUUUUUU
        IIIIIIIIIIIIIII
        '''


        ale = random.choice(cartas)
        start = input("--->")
        print("casa tirou: ", ale)
        casa = ale + casa
        print("pontuação da casa: ", casa)

    #teste caso casa perdeu
    if casa > 21:
        print(f"Voce ganhou com {player} pontos, a casa perdeu com {casa} pontos.")
        print(f"Voce ganhou {aposta * 2} reais.")
        dinheiro = dinheiro + aposta
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break

    #mostrar pontos da casa e comparar pra ver quem ganhou
    print(f"Casa tem {casa} pontos")
    start = input("--->")
    print("vamos comparar")
    start = input("--->")
    if player > casa:
        print(f" VOCE GANHOU {aposta * 2 } reais. voce tem {player} pontos e a casa tem {casa} pontos")
        dinheiro = dinheiro + aposta
    else:
        print(f"voce perdeu {aposta} reais, a casa tem {casa} pontos e voce tem {player} pontos")
        dinheiro = dinheiro - aposta

    acao = input("jogar de novo? y/n: ")
    if acao == "y":
        continue
    elif acao == "n":
        break

print("obrigado por jogar")
