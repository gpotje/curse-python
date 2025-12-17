
lista = ['M','H','L']

n1, n2, n3 = lista #desempacotar a lista 
n1, n2, n3 = ['M','H','L']
n1, *resto = ['M','H','L']
n1, *_ = ['M','H','L']
_ ,n1, *_ = ['M','H','L']

for index, item  in enumerate(lista):
    print(f'{index} - {item}')