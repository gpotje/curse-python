"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Enter with a number:')

try:
    numero = int(entrada)
    if numero  % 2 == 0:
        print(f"'{numero}'The number enter is par.")
    else:
       print(f"'{numero}'The number enter is impar.") 

except ValueError:
    print(f"'{entrada}' The number entered is not available.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('enter what time is it only numeric int:')

try:
    numero = int(entrada)
    if len(numero) > 0 and len(numero) < 11:
        print('Good morning')

    elif  len(numero) > 11 and len(numero) < 18:
        print('good afternoon')

    else:
     print('good night') 

except ValueError:
    print(f"'{entrada}' The number entered is not available.")






"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('What is you name?:')


if len(name) < 4:
    print('Your name is so short')

elif  len(name) > 4 and len(name) < 7:
    print('Your name is normal')

else:
  print('Your name is so big') 





