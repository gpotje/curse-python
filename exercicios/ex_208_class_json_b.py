import json
from ex_208_class_json_a import Pessoa



with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    p1 = json.load(arquivo)

p2 = Pessoa(p1['nome'],p1['idade'])

print(Pessoa.printa_pessoa(p2))