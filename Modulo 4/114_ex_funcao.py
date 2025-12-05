
def mulNumber(*args):
    total = 1 
    for i in args:
        total *=  i
    
    return total



print(mulNumber(1,2,3,4))