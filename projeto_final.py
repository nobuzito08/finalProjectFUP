import random

#Proximos passos(acho que o bruto finalmente acabou ;), foi bem dificl (meu deus nao acabou, o que ta dando errado) :
#Fazer split
#comentar e mudar nomes de variaves para ficar mais legivel(em processo)
#ver se o "ale" e realmente nessesario, ou se ele pode exisitr apenas no escopo da função


#AVISO!!!!!!
#eu de vez em quando chamo dicionarios de bibliotecas, sempre que eu falei biblioteca aqui eu quis dizer dicionario, tentei da uma procurada por esses erros e acho que achei a maioria, mas posso ter deixado algum passar



dinheiro = 50

#Função para comprar cartas
def dealar(Aleatorio:int,Total:int):
    #Tira um numero aleatorio de 0 ate o numero de cartas que tem(no inicio e 51)
    Aleatorio = random.randint(0,numCartasSobrando)
    
    #Passa o valor da carta tirada para "valor"
    Valor = cartas[Aleatorio]['valor']
    
    #Passa o hexcode da carta para "carta"
    carta = cartas[Aleatorio]['card']

    #Testa para ver se a carta e um ás e se ele vai ter valor de 1 ou 11. Depois soma ao total
    if (Total + Valor) > 21 and Valor == 11:
        Total = Valor + Total - 10
    else:
        Total = Valor + Total
        
    #Retorna os pontos que vc ja tinha + carta nova, o hexcode da carta que vc tirou, e a poscição da carta no vetor
    return Total, carta, Aleatorio, Valor

#função para dar .append da nova carta para os vetores que guardam as cartas da sua mao e os valores dela, alem de tirar essa carta da bibilhoteca do baralho, para ela nao ser tirada de novo
def acrescentador (Aleatorio:int, Valores, Cards, Baralho, CartasSobrando:int):
    #adiciona o valor da carta ao vetor "valores"
    AuxValores = Baralho[Aleatorio]['valor']
    Valores.append(AuxValores)
    
    #adiciona o hexcode da carta ao vertr "cards"
    AuxCards = Baralho[Aleatorio]['card']
    Cards.append(AuxCards)
    
    #tira a carta do baralho, para ela nao ser tirada de novo
    del Baralho[Aleatorio]
    CartasSobrando = CartasSobrando -1
    
    #retorna o vetorValores + valor da carta nova, e o vetorCard + hexcode da carta nova, depois atualiza o baralho para ficar sem a carta retirada e anota que o baralho tem uma carta a menos.
    return Valores, Cards, Baralho, CartasSobrando

#função para formatar os saves antigos + save atual
def encode(AtualGeral):
    #Variavel onde vai ficar o texto que posteriormente vai ser escrito no arquivo
    RankingFormatado = ''
    
    #pegando cada biblioteca ('i') dentro do vetor com os saves antigos + o novo, e formatando para escrever no arquivo
    for i in AtualGeral:
        RankingFormatado += f"{i['nome']};{i['dinheiro']}\n"
    return RankingFormatado

#função para transformar em vetor e dicionarios o texto do arquivo com os saves antigos
def decode(Lodados):
    #vetor onde vai ficar os dicionarios com os saves
    auxVetor = []
    
    #splitando e transformando em dicionario os dados no arquivo.txt com os rankings
    for salvamentos in Lodados:
        salvamentos = salvamentos.strip()
        dados = salvamentos.split(';')
        auxDicio = {
            'nome' : dados[0],
            'dinheiro' : int(dados[1])
        }
        
        #adicionando o dicionario modificado com os dados do aquivo.txt a um vetor
        auxVetor.append(auxDicio)
    return auxVetor

#pega os saves antigos
def load():
    arquivo = open("C:/Users/LEON/Documents/UFC/leaderBord/Ranking.txt",'r')
    saves = arquivo.readlines()
    arquivo.close()
    return saves



#meu maior terror pesadelo de todos os tempos: função para salvar
def save(Saves, SaveAtual):
    #ok, isso demorou muito mais do que pensava para fazer, acabei precisando fazer algumas funçoes a mais pra fazer isso funcionar, vai da um trabalho esplicar o que tava pensando durante esses dias de maneira coerente.
    #vou tentar fazer bem passo a passo pra facilitar o entendimento, qualquer coisa desculpe
    
    #abrindo o arquivo txt com os rankings
    arq = open("C:/Users/LEON/Documents/UFC/leaderBord/Ranking.txt",'w')
    
    #Vetor onde vai ficar a lista de saves antigos com o save novo no meio
    auxVetor = []
    
    #contador pra saber aonde precisamos adicionar o nome do jogador atual na lista de saves, quando o dinheiro do jogador atual e maior do que o dinheiro do save pela primeira vez, ele adiciona o nome do jogador atual e logo depois adiciona o nome do jogador do save antigo, depois disso ele nunca mais adiciona o nome do jogador atual de novo, ele so segue adicionando os nomes e valores do resto dos jogadores do save antigo
    counter = 0
    
    #pega a informação do arquivo txt, arruma em um vetor de dicionarios, e depois adiciona na variavel 'savesDecodados'
    SavesDecodados = decode(Saves)
    
    #para cada biblioteca com o nome e o dinheiro do jogador dentro do vetor com os saves antigos ele executa o que ta dentro desse for
    for save in SavesDecodados:
        
        #se o dinheiro do jogador do save antigo for maior do que o atual, ele adiciona o dicionario do jogador antigo em um vetor (auxVetor)
        if save['dinheiro'] > SaveAtual['dinheiro']:
            auxVetor.append(save)
        
        # se o dinheiro do jogador do save antigo for menor, e se o contador for igual a 0, adiciona o nome do jogador atual, e depois o nome do jogador antigo que o jogador atual foi comparado
        elif counter == 0:
            
            #so adiciona o jogador novo se ele nao aparecer nos saves antigos, se nao fizer isso pode ficar duplicando a mesma pessoa varias vezes
            if SaveAtual != save:
                auxVetor.append(SaveAtual)
                auxVetor.append(save)
            
            #se forem a mesma pessoa, so adiciona o nome antigo, pois assim so fica um nome no vetor final, e nao da pra ficar duplicando
            else:
                auxVetor.append(save)
            
            #contador agora e diferente de 1, agora mesmo se o dinheiro do jogador antigo for menor que o do jogador novo, no proximo loop do for o jogador novo nao vai ser adicionado de novo e a lista vai completar com os nomes que faltam
            counter = counter + 1
        
        #completando o vetor com os nomes que faltam
        else:
            auxVetor.append(save)
    
    #salvar se for o ulitmo 
    if counter == 0:
        auxVetor.append(saveAtual)
    
    #formata o vetor de dicionarios em uma string para ser escrita no arquivo.txt
    AtualEncodado = encode(auxVetor)
    
    #escreve a strig com todos os saves antigos mais o novo no arquivo
    arq.write(AtualEncodado)
    
    #fecha o arquivo
    arq.close()


#nome do jogador
nome = ''

#perguntando o nome do jogador
nome = str(input('Digite seu nome: '))

while dinheiro > 0:
    #dicionario de todas as cartas(fiz as 5 primeiras e pedi pra IA fazer o resto do baralho, como nao pede nenhuma logica, sendo so trabalho bruto, achei inteligente fazer isso.)
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


    #outras variaveis
    
    #O numero de cartas sobrando, pra saber o limite do random.randint
    numCartasSobrando = 51
    
    #auxiliar, geralmente segura o valor aleatorio gerado pelo random.randint(pocisao da carta na biblioteca)
    aux = 0
    
    #auxiliar em formato string, geralente segura o hexcode da carta retirada
    auxStr = ''
    
    #total de pontos do jogador
    player = 0
    
    #valores das cartas na mao do jogador
    valoresMao = []
    
    #cartas na mao do jogador
    cardMao = []
    
    #total de pontos da casa
    casa = 0
    
    #valores das cartas na mao da casa
    valoresCasa = []
    
    #cartas ba nai da casa
    cardCasa = []
    
    #variavel para fazer "= input('---->')", feito pra da uma ritimada melhor no jogo
    start = 0
    
    #variavel para segurar o valor aleatorio do random.randint dentro da função (nao tenho certeza se e nessesario, preciso olhar depois)
    ale = 0
    
    #variavel para saber o que o jogador vai fazer ("hit", "duble", "hit and duble")
    acao = '0'
    
    #mais uma auxiliar para salvar o valor da carta retirada, posso procurar otimizar isso depois
    auxValor = 0
    
    #tela de entrada
    print('Bem vindo ao blackjack \U0001F0A1 \U0001F0B1 \U0001F0C1 \U0001F0D1')
    
    

    #enter pra iniciar o jogo
    start = input('"ENTER" pra jogar:')
    print(f"Você tem {dinheiro} reais")
    
    #aposta
    while True:
        aposta = (input("Quanto vc aposta:"))
        if aposta.strip() == '':
            aposta = 0
        else:
            aposta = int(aposta)
        if aposta > dinheiro:
            print("Nao aposte mais do que tem")
        else:
            break


    #mostrar a pontuação da casa com uma carta
    casa, auxStr, aux, auxValor = dealar(ale, casa,)
    valoresCasa, cardCasa, cartas, numCartasSobrando = acrescentador(aux,valoresCasa,cardCasa,cartas,numCartasSobrando)
    print (f"Casa: {cardCasa}({auxValor}), X")
    
    #tirar a segunda carta e somar com o total da casa
    casa, auxStr, aux, auxValor = dealar(ale, casa)
    valoresCasa, cardCasa, cartas, numCartasSobrando = acrescentador(aux,valoresCasa,cardCasa,cartas,numCartasSobrando)

    start = input("--->")

    #mostrar as duas primeiras cartas
    player, auxStr, aux, auxValor = dealar(ale, player)
    valoresMao, cardMao, cartas, numCartasSobrando = acrescentador(aux,valoresMao,cardMao,cartas,numCartasSobrando)
    print (f'Voce: {cardMao}({player})')
    player, auxStr, aux, auxValor = dealar(ale, player)
    valoresMao, cardMao, cartas, numCartasSobrando = acrescentador(aux,valoresMao,cardMao,cartas,numCartasSobrando)
    print (f'Voce: {cardMao}({valoresMao}), total:{player}')
    
    #em caso de balackjack
    if player == 21:
        print(f"VOCE GANHOU COM UM BLACKJACK")
        print(cardMao)
        dinheiro = dinheiro + aposta 
        
        #reiniciar ou terminar o jogo
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break

    while acao != "":
        
        #Ação do jogador
        acao = (input("O que fazer: Hit = 1, Double = 2, Hit and Double = 3, nada pra continuar:  "))
        match acao:
            case "1":
                
                #adicionar uma carta a mão
                player, auxStr, aux, auxValor = dealar(ale,player,)
                valoresMao, cardMao, cartas, numCartasSobrando = acrescentador(aux,valoresMao,cardMao,cartas,numCartasSobrando)
                print(f'voce tirou um {auxStr}({auxValor})')
            case "2":
                
                #dobra a aposta
                aposta = aposta * 2
                print("sua aposta agora é: ", aposta)
            case "3":
                
                #adiciona uma carta a mão e dobra a aposta
                player, auxStr, aux, auxValor = dealar(ale,player,)
                valoresMao, cardMao, cartas, numCartasSobrando = acrescentador(aux,valoresMao,cardMao,cartas,numCartasSobrando)
                print(f'voce tirou um {auxStr}({auxValor})')
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
    print(f"pontuacao total da casa é: {casa},({valoresCasa},{cardCasa})")
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

        start = input("--->")

        #adicionar uma carta a mao da casa
        casa,auxStr, aux, auxValor = dealar(ale,casa)
        print (f'casa tirou {auxStr}({auxValor})')
        print (f'total casa: {casa}, ({cardCasa}, {valoresCasa})')

    #teste caso casa perdeu
    if casa > 21:
        print(f"Voce ganhou com {player} pontos ({cardMao}, {valoresMao}), a casa perdeu com {casa} pontos ({cardCasa}, {valoresCasa}).")
        print(f"Voce ganhou {aposta * 2} reais.")
        dinheiro = dinheiro + aposta
        acao = input("jogar de novo? y/n: ")
        if acao == "y":
            continue
        elif acao == "n":
            break

    #mostrar pontos da casa e comparar pra ver quem ganhou
    print(f"Casa tem {casa} pontos ({cardCasa}, {valoresCasa})")
    start = input("--->")
    print("vamos comparar")
    start = input("--->")
    if player > casa:
        print(f" VOCE GANHOU {aposta * 2 } reais. voce tem {player} pontos e a casa tem {casa} pontos")
        dinheiro = dinheiro + aposta
    else:
        print(f"voce perdeu {aposta} reais, a casa tem {casa} pontos e voce tem {player} pontos")
        dinheiro = dinheiro - aposta
        
    #decidindo se vai jogar de novo ou fechar o jogo
    acao = input("jogar de novo? y/n: ")
    if acao == "y":
        continue
    elif acao == "n":
        break

#textando se o wile quebrou por escolha, ou poque seu dinheiro acabou
if dinheiro == 0:
    print("voce perdeu todo seu dinheiro, estao te explusando do cassino, vai trabalhar.")
    print('...')
    print('')

#biblioteca com o nome e o dinheiro do jogador atual
saveAtual = {'nome': nome, 'dinheiro' : dinheiro}

#puxando os saves antigos
savesAntigos = load()

#usando a função mais do mal que exite para salvar o jogo
save(savesAntigos, saveAtual)

#pegando os saves para mostrar uma leaderbord
decodados = decode(savesAntigos)
print ('leaderbord: ')

#mostrando bonitinho a leaderbord
for i in decodados:
    print(f'Nome: {i['nome']}, Dinheiro: {i['dinheiro']}')


print("obrigado por jogar")

print('')