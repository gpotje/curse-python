name = input('Enter your name:')
age = input('Enter your age:')
reveserd = name[::-1] #revesed in python
space_count = name.count(" ")
character_count = len(name)
first_char = name[0]
last_char = name[-1]

if name != '' and age != '':

    print('tranks for type your name')
    print('your name is:',name)
    print('your name reversed is:',reveserd)
    print('The number os spaces in the string is:',space_count)
    print(f'your name: {name} has {character_count} characters')
    print('The first letter your name is:',first_char)
    print('The last letter your name is:',last_char)

else:
    print('how you dont type your name, ' \
    'its program termined now!!')



    