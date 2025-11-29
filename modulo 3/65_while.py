name = input('What your name?')

number = len(name)
count = 0
new_name = ''

while count < number:
    print(f'{name[count]}*',end="")
    new_name +=name[count]+"*"
    count = count + 1

print()   

print(f'your name has: {number}')    
print(f'your new name is: {new_name}')   