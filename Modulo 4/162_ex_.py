# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


produtos_2 = produtos 

for i,produto in enumerate(produtos_2):
    valor = float(produto['preco'])

    div = valor / 100
    mul = div * 10
    valor = valor + mul

    produto['preco'] = round(valor, 2)

    produtos[i]  = produto


#print(f'========={produtos}')

#Ordenar decrescente:(do maior para menor)
lista_ordenada = sorted(produtos, key=lambda x: x["nome"], reverse=True)

print(f'\n=====Ordenar decrescente campo nome====:\n{lista_ordenada}\n')

#Ordenar crescente:(do menor para maior)
lista_ordenada_2 = sorted(produtos, key=lambda x: x["preco"])

print(f'\n====Ordenar crescente:(do menor para maior) campo preço=====:\n{lista_ordenada_2}\n')
    

