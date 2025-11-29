from modulo import clear_terminal

list_shop = []
exit = False

def listar(list_shop):
    if not list_shop:
        print("The list is blank.")
    else:
        for i, item in enumerate(list_shop):
            print(f'{i} - {item}')


def apagar(list_shop_func,indice):
     if not list_shop_func:
        print("Deleting an item from an empty list is no possible: ")
     else:
        list_shop_func.pop(indice)
       

   
def inserir(list_shop_func,item):
    list_shop_func.append(item)
    

def choose(list_shop_func,option):
     match option:
        case 'i':
            item = input('Please enter a new item: ') 
            inserir(list_shop_func,item)
        case 'd':
            index = int(input('Enter the index of the item you want to delete: '))
            apagar(list_shop_func,index)
        case 'l':
            listar(list_shop_func)
        case 'c':
            clear_terminal()
        case 'e':
            exit = True
        case _: 
            return "The value type is not valid"

while exit != True:
    print('Choose an option below')
    option = input('[i]nsert [d]elete [l]ist [e]xit [c]lean:')
    choose(list_shop,option)
