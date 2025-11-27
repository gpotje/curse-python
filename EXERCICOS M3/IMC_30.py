# pip install keyboard

print('Digite seu nome:')
nome = input()

print('Digite seu peso:')
peso = float(input()) 

print('Digite sua altura:')
altura = float(input()) 

altura_ao_quadrado = altura  ** 2
imc = peso / altura_ao_quadrado 


print(f'Seu IMC é: {imc:.2f}')


