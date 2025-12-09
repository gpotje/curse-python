# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from json_208_a import CAMINHO_ARQUIVO,Pessoa



with open(CAMINHO_ARQUIVO,'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(p1.nome,p1.idade)
    print(p2.nome,p2.idade)