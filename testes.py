def save(Saves, SaveAtual):
    arq = open("C:/Users/LEON/Documents/UFC/leaderBord/Ranking.txt",'w')
    auxVetor = []
    counter = 0
    SavesDecodados = decode(Saves)
    for save in SavesDecodados:
        if save['dinheiro'] > SaveAtual['dinheiro']:
            auxVetor.append(save)
        elif counter == 0:
            if SaveAtual != save:
                auxVetor.append(SaveAtual)
                auxVetor.append(save)
            else:
                auxVetor.append(save)
            counter = counter + 1
        else:
            auxVetor.append(save)
    AtualEncodado = encode(auxVetor)
    arq.write(AtualEncodado)
    arq.close()
        
def load():
    arquivo = open("C:/Users/LEON/Documents/UFC/leaderBord/Ranking.txt",'r')
    saves = arquivo.readlines()
    arquivo.close()
    return saves

def decode(Lodados):
    auxVetor = []
    for salvamentos in Lodados:
        salvamentos = salvamentos.strip()
        dados = salvamentos.split(';')
        auxDicio = {
            'nome' : dados[0],
            'dinheiro' : int(dados[1])
        }
        auxVetor.append(auxDicio)
    return auxVetor

def encode(AtualGeral):
    RankingFormatado = ''
    for i in AtualGeral:
        RankingFormatado += f"{i['nome']};{i['dinheiro']}\n"
    return RankingFormatado
        
    
saveDeAgora = {'nome': 'joa', 'dinheiro' : 500}

savesPassados = load()
save(savesPassados, saveDeAgora)

decodados = decode(savesPassados)
print (decodados)