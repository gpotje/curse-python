# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = '208_aula.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade 

p1 = Pessoa('Gabriel',33)
p2 = Pessoa('Gleice',35)

bd = [p1.__dict__,vars(p2)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO,'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd,arquivo,ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()