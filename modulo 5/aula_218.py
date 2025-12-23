#Composição

class Cliente: 

    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inseri_enderece(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))


    def lista_endereco(self):
        print('Cliente: '+self.nome)
        print('=========== Endereços ===========')
        for e in self.enderecos:
            print(e.rua, e.numero)  
        print('=========== ========= ===========')

class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua
        self.numero = numero


c1 = Cliente('Gabriel')
c1.inseri_enderece('estrada','200')
c1.inseri_enderece('sueo','201')

c1.lista_endereco()