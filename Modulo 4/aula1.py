print('Hello,world')
#how to config python for windonw
P#S C:\Users\gpotj> Get-ExecutionPolicy
#Restricted
#python -m venv venv
#Set-ExecutionPolicy AllSigned -Force
#.\venv\Scripts\activate
#cd C:\Users\gpotj\Desktop\python
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#.\venv\Scripts\Activate.ps1
# def imprimir(a,b,c):
    
#     print(f'eai {a,b,c}')


# imprimir('teste',3,4)
    
#*args
def sum(*args):
    total = 0
    for numero in args:
        total = total + numero
    
    return total

print(sum(1,3,5,6))


