#empacotamento e desempacotamento de dicionários 
#*args e **kwargs

def mostros_argumentos_nomeados(*args,**kwargs):
    print('NÃO NOMEADOS:',args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostros_argumentos_nomeados(1,2, nome='joana', qlq=123)

config = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4, 
}

mostros_argumentos_nomeados(config)
print("=============================")
mostros_argumentos_nomeados(*config)
print("=============================")
mostros_argumentos_nomeados(**config)