import json

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def printa_pessoa(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'



p1 = Pessoa('Gabriel',29)

with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
     json.dump(p1.__dict__, arquivo, ensure_ascii=False, indent=4)

