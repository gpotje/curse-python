
import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# print(pessoa)
# pessoa['nome'] = 'gabriel'
# pessoa['enderecos'][0]['rua'] = 'Rua Nova'
# print(pessoa)

# with open('dados.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)



with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados_python = json.load(arquivo)


print(dados_python)
# pessoa['nome'] = 'gabriel'
# pessoa['enderecos'][0]['rua'] = 'Rua Nova'
# print(pessoa)
