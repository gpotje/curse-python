

class MinhaString(str):
    def upper(self):
        print('CHAMANDO...')
        return super().upper()

s = MinhaString('teste')
print(s.upper())
        

class A:
    valor_a = "valor a"

    def metodo(self):
        print("A")

class B(A):
    # B tem 'valor_a = "valor a"'
    valor_b = "valor b"

    # B sobreescreveu o metodo a
    def metodo(self):
        print("B")
    
class C(B):
    # C tem 'valor_a = "valor a"'
    # C tem 'valor_b = "valor b"'
    valor_c = "valor c"

    # C sobreescreveu o metodo a
    def metodo(self):
        print("C")


c1 = C
print(c1.valor_a, c1.valor_b, c1.valor_c)
c1.metodo('e')