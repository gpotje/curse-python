# install library to use keybord
# pip install keyboard
questions = [

    {
        'question' : 'how much is 2+2 ?',
        'option'  : ['1','2','3','4'],
        'answer'  : '4',
    },
    {
        'question' : 'how much is 5*5 ?',
        'option'  : ['25','55','10','51'],
        'answer'  : '25',
    },
    {
        'question' : 'how much is 10/2 ?',
        'option'  : ['4','5','2','1'],
        'answer'  : '5',
    }


]

for q in questions:
    print(q['question'])
    

    # for i, s in enumerate(q['option']):
    #     print(f'{i})' , s)
    # print()

    d1 = input('type your answer here...')

    if d1 == q['answer']:
        print("Is correct!")
    else:
        print("Response isn't correct: "+q['answer'])
    print()

print('create by Gabriel Potje')


