class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def andar(self):
        print(f'{self.nome} está andando')

p1 = Pessoa('João','Silva')

print(p1.nome)
print(p1.sobrenome)
p1.andar()
        
# p1 = Pessoa('Maria','Souza')

# print(p1.nome)
# print(p1.sobrenome)
# p1.andar()

print(p1.__dict__)
print(vars(p1))