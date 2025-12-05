"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

sumCpf = 0

cpf = list('746.824.890-70')
cpfWithOutDotDash = ''

cpfWithOutDotDash = cpf[0]+cpf[1]+cpf[2]
cpfWithOutDotDash = cpfWithOutDotDash+ cpf[4]+cpf[5]+cpf[6]
cpfWithOutDotDash = cpfWithOutDotDash+ cpf[8]+cpf[9]+cpf[10]
#cpfWithOutDotDash = cpfWithOutDotDash+ cpf[12]+cpf[13]

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

