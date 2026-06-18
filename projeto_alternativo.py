

#sistema de gerenciamento de biblioteca de jogos

#To do list:
#Melhorar o sistema de busca, acho que posso fazer o sistema de busca que divide pela metade
#Quando adicionar um jogo, ja botar em ordem alfabetica(n tenho ideia de como fazer)

def save(Jogos):
    arquivo = open('dados.txt', 'w')
    for jogo in jogos:
        arquivo.write(f'{jogo['nome']};')
        arquivo.write(f'{jogo['autor']};')
        arquivo.write(f'{jogo['editor']};')
        arquivo.write(f'{jogo['preco']};')
        arquivo.write(f'{jogo['lancamento']};')
        arquivo.write(f'{jogo['genero 1']};')
        arquivo.write(f'{jogo['genero 2']}/n')

def load():
    arquivo = open('dados.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        palavras = linha.split(';')
        jogo['nome'] = palavras[0]
        jogo['autor']
        jogo['editor']
        jogo['preco']
        

def busca(Pesquisa, Jogos):
    contador = 0
    while contador != 1:
        for jogo in jogos:
            if jogo['nome'].startwith(f'{Pesquisa}'):
                jogo 






jogos = []
auxVetor = []
auxBiblioteca = {}
auxStr = ''
aux = 0
tamplateBiblioteca = {
    'nome' : 'nome jogo',
    'autor' : 'nome autor',
    'editor' : 'nome editor',
    'preco' : 0.0,
    'lancamento' : '00/00/2000',
    'genero 1' : 'genero',
    'genero 2' : 'genero dois'
    }
count = 0

acao = str(input('1-Gerenciar Biblioteca \n2-procurar um jogo por nome \n3-procurar um jogo por genero \n0-sair \n:'))

while acao != 0 :
    match acao:
        case '1':
            print('')
            print('Gerenciar Biblioteca')
            print('...')
            acao = str(input('escolha a ação a fazer: \n1-adicionar um jogo, \n2-remover um jogo \n3-editar um jogo \n:'))
            
            match acao:
                case '1':
                    
                    print ('Adicionar um jogo: ')
                    print ('')
                    
                    tamplateBiblioteca['nome'] = str(input('Insira o nome do jogo: '))
                    tamplateBiblioteca['autor'] = str(input('Insira o nome do autor: '))
                    tamplateBiblioteca['editor'] = str(input('Insira o nome do editor: '))
                    tamplateBiblioteca['preco'] = float(input('Insira o preco: '))
                    tamplateBiblioteca['lancamento'] = str(input('Insira a data de lancamento(formato: DD/MM/AAAA): '))
                    auxStr = str(input('escolha um dos generos: \n1-Ação, \n2-Aventura, \n3-Tiro, \n4-RPG, \n5-Estrategia, \n6-Simulação, \n7-Sandbox, \n8-Puzzle, \n9-Luta \n:'))
                    
                    match auxStr:
                        case '1':
                            tamplateBiblioteca['genero 1'] = 'Ação'
                            auxStr = ''
                        case '2':
                            tamplateBiblioteca['genero 1'] = 'Aventura'
                            auxStr = ''
                        case '3':
                            tamplateBiblioteca['genero 1'] = 'Tiro'
                            auxStr = ''
                        case '4':
                            tamplateBiblioteca['genero 1'] = 'RPG'
                            auxStr = ''
                        case '5':
                            tamplateBiblioteca['genero 1'] = 'Estratégia'
                            auxStr = ''
                        case '6':
                            tamplateBiblioteca['genero 1'] = 'Simulação'
                            auxStr = ''
                        case '7':
                            tamplateBiblioteca['genero 1'] = 'Sandbox'
                            auxStr = ''
                        case '8':
                            tamplateBiblioteca['genero 1'] = 'Puzzle'
                            auxStr = ''
                        case '9':
                            tamplateBiblioteca['genero 1'] = 'Luta'
                            auxStr = ''
                    
                    auxStr = str(input('escolha o segundo genero: \n1-Ação, \n2-Aventura, \n3-Tiro, \n4-RPG, \n5-Estrategia, \n6-Simulação, \n7-Sandbox, \n8-Puzzle, \n9-Luta \n:'))
                    
                    match auxStr:
                        case '1':
                            tamplateBiblioteca['genero 2'] = 'Ação'
                            auxStr = ''
                        case '2':
                            tamplateBiblioteca['genero 2'] = 'Aventura'
                            auxStr = ''
                        case '3':
                            tamplateBiblioteca['genero 2'] = 'Tiro'
                            auxStr = ''
                        case '4':
                            tamplateBiblioteca['genero 2'] = 'RPG'
                            auxStr = ''
                        case '5':
                            tamplateBiblioteca['genero 2'] = 'Estratégia'
                            auxStr = ''
                        case '6':
                            tamplateBiblioteca['genero 2'] = 'Simulação'
                            auxStr = ''
                        case '7':
                            tamplateBiblioteca['genero 2'] = 'Sandbox'
                            auxStr = ''
                        case '8':
                            tamplateBiblioteca['genero 2'] = 'Puzzle'
                            auxStr = ''
                        case '9':
                            tamplateBiblioteca['genero 2'] = 'Luta'
                            auxStr = ''
                    
                    #adiciona o novo jogo ao vetor de jogos   
                    jogos.append(tamplateBiblioteca)        
                    
                    #Mostra as informações do jogo adicionado
                    for key in tamplateBiblioteca.keys:
                        print(tamplateBiblioteca.items)
                    
                    
                    acao = ''
                case '2':
                    print ('Remover um jogo: ')
                    print ('')
                    
                    auxStr = str(input('escolher por nome do jogo(digite:jogo), \npor nome do autor(digite:autor) \npor nome de editor(digite:editor) \npor preco(digite:preço) \n ou por genero(digite genero)'))
                    
                    
                    
                    acao = ''
                    
                    match auxStr:
                        case 'jogo':
                            auxStr = str(input('Digite o nome: '))
                            
                            while count != 1:
                                for jogo in jogos:
                                    if jogo['nome'].startwith(auxStr):
                                        auxBiblioteca =jogo
                                        auxVetor.append(auxBiblioteca)
                                print ('jogos encontrados: ')
                                if len(auxVetor) == 0:
                                    print ('nada encontrado')
                                    count = 1
                                else:
                                    for iten in auxVetor:
                                        print (f' numero {iten}-{auxVetor[iten]}')
                                    aux = int(input('qual jogo escolher (digite o numero): '))
                                    print ('jogo escolhido: \n', auxVetor[aux])
                                    auxStr = str(input('Deletar jogo? (y/n): '))
                                    if auxStr == 'y':
                                        jogos.remove(auxVetor[aux])
                                        count = 1
                                    auxStr = str(input(('jogo nao deletado, quer tentar de novo?(y/n)')))
                                    if auxStr == 'n':
                                        count = 1


                                    
                                
                            