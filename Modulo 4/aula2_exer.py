
#exercicios
#Crie  funções que duplicam, triplicam e quadruplicam
# o numero recebido como parametros

def mult_number(multiplicador):
    def mutiplicar(number):
        return number * multiplicador
    return mutiplicar

duplicar      = mult_number(2)
triplicar     = mult_number(3)
quadruplicar  = mult_number(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


