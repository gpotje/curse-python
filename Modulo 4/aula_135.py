#sort tradicional 
#criação de um comparador

# lista = [1,35,92,396,927,25,36]
# lista.sort()

# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

def exibir(lista):
    for item in lista:
        print(item)
    print()


lista.sort(key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista)
exibir(l2)