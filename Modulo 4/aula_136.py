def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y


print(
    executa(
        lambda x, y: x + y,
        2,3
    )

)