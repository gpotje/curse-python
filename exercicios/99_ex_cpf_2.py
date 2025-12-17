"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
sumCpf = 0

cpf = list('746.824.890-70')
cpfWithOutDotDash = ''

cpfWithOutDotDash = cpf[0]+cpf[1]+cpf[2]
cpfWithOutDotDash = cpfWithOutDotDash+ cpf[4]+cpf[5]+cpf[6]
cpfWithOutDotDash = cpfWithOutDotDash+ cpf[8]+cpf[9]+cpf[10]
cpfWithOutDotDash = cpfWithOutDotDash+ cpf[12]

sumCpf = list(cpfWithOutDotDash)

print(cpfWithOutDotDash)

sum2 = 0
count = 10

print(sumCpf)

for i in  sumCpf:
    numero = int(i)
    sum2 = sum2 + (numero * count)
    print(f'--numero: {numero} X count: {count} soma: {numero*count}  -- acumulado: {sum2}')
    count = count - 1 

sum2 = sum2 * 10
verificaCpf = sum2 % 11

if  verificaCpf == int(cpf[12]) :
    print(f"Cpf é valido")
else:
    print(f"Cpf Não valido")

