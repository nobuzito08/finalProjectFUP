

#sistema de gerenciamento de biblioteca de jogos

jogos = []
auxBiblioteca = {
    'nome' : 'nome jogo',
    'autor' : 'nome autor',
    'editor' : 'nome editor',
    'preco' : 0.0,
    'lancamento' : '00/00/2000',
    'genero 1' : 'genero',
    'genero 2' : 'genero dois'
    }
auxAcao = ''

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
                    auxBiblioteca['nome'] = str(input('Insira o nome do jogo: '))
                    auxBiblioteca['autor'] = str(input('Insira o nome do autor: '))
                    auxBiblioteca['editor'] = str(input('Insira o nome do editor: '))
                    auxBiblioteca['preco'] = float(input('Insira o preco: '))
                    auxBiblioteca['lancamento'] = str(input('Insira a data de lancamento(formato: DD/MM/AAAA): '))
                    auxAcao = str(input('escolha um dos generos: \n1-Ação, \n2-Aventura, \n3-Tiro, \n4-RPG, \n5-Estrategia, \n6-Simulação, \n7-Sandbox, \n8-Puzzle, \n9-Luta \n:'))
                    
                    match auxAcao:
                        case '1':
                            auxBiblioteca['genero 1'] = 'Ação'
                            auxAcao = ''
                        case '2':
                            auxBiblioteca['genero 1'] = 'Aventura'
                            auxAcao = ''
                        case '3':
                            auxBiblioteca['genero 1'] = 'Tiro'
                            auxAcao = ''
                        case '4':
                            auxBiblioteca['genero 1'] = 'RPG'
                            auxAcao = ''
                        case '5':
                            auxBiblioteca['genero 1'] = 'Estratégia'
                            auxAcao = ''
                        case '6':
                            auxBiblioteca['genero 1'] = 'Simulação'
                            auxAcao = ''
                        case '7':
                            auxBiblioteca['genero 1'] = 'Sandbox'
                            auxAcao = ''
                        case '8':
                            auxBiblioteca['genero 1'] = 'Puzzle'
                            auxAcao = ''
                        case '9':
                            auxBiblioteca['genero 1'] = 'Luta'
                            auxAcao = ''
                    
                    auxAcao = str(input('escolha o segundo genero: \n1-Ação, \n2-Aventura, \n3-Tiro, \n4-RPG, \n5-Estrategia, \n6-Simulação, \n7-Sandbox, \n8-Puzzle, \n9-Luta \n:'))
                    
                    match auxAcao:
                        case '1':
                            auxBiblioteca['genero 2'] = 'Ação'
                            auxAcao = ''
                        case '2':
                            auxBiblioteca['genero 2'] = 'Aventura'
                            auxAcao = ''
                        case '3':
                            auxBiblioteca['genero 2'] = 'Tiro'
                            auxAcao = ''
                        case '4':
                            auxBiblioteca['genero 2'] = 'RPG'
                            auxAcao = ''
                        case '5':
                            auxBiblioteca['genero 2'] = 'Estratégia'
                            auxAcao = ''
                        case '6':
                            auxBiblioteca['genero 2'] = 'Simulação'
                            auxAcao = ''
                        case '7':
                            auxBiblioteca['genero 2'] = 'Sandbox'
                            auxAcao = ''
                        case '8':
                            auxBiblioteca['genero 2'] = 'Puzzle'
                            auxAcao = ''
                        case '9':
                            auxBiblioteca['genero 2'] = 'Luta'
                            auxAcao = ''
                    acao = ''
print(auxBiblioteca)