from modulo import clear_terminal

numero = int(input('entre com um numero para tabuada: '))
r = 0
exit = ''
sair = False

while sair == False:

    print()

    for i in range(11):
        r = numero*i
        print(f'{numero} X {i} = {r}')

    print()
    exit = input('Do you want to exit [y] ? ')
   
    if exit == 'y':
        sair = True
        print('Até a proxima !! ')

    else:
        clear_terminal()
        numero = int(input('entre com um numero para tabuada: '))