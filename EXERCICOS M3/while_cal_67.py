n1 = 0
n2 = 0  
operador = 0
exist = ''



while exist != 'y':

    n1 = float(input("Enter with 1° number: "))
    n2 = float(input("Enter with 2° number: ")) 

    r  = 0
    print('choose one of option:')
    print('1) sum')
    print('2) minus')
    print('3) multiplication')
    print('4) division')

    entrada = input()

    print()

    try:
        operador = int(entrada)
        if operador == 1:
            r = n1+n2
            print(f'{n1} + {n2} = {r}')
        elif operador == 2:
            r = n1-n2
            print(f'{n1} - {n2} = {r}')
        elif operador == 3:
            r = n1*n2
            print(f'{n1} X {n2} = {r}')
        elif operador == 4:
            r = n1/n2
            print(f'{n1} / {n2} = {r}')
        else:
            print(f'The entered number is invalid.')

    except ValueError:
        print(f"'{entrada}' The entered value is invalid.")
   

    exist = input('Do you want to exist [y] ?')

