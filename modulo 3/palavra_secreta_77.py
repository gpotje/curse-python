"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

secret_word = input('Digite uma palavra secreta:')
format_word = "*" * len(secret_word)
new = list(format_word)
print_palavra = ''
count = 0
quant = 0
fim_excucao = False
palavra_final = ''


letter = input('Enter with only one letter:')



print(format_word)



while fim_excucao == False:
    
    if count == len(secret_word):
        print(palavra_final)
        letter = input('Enter with only one letter:')
        count = 0

    for i in range(len(secret_word)):
        count = count + 1
        if secret_word[i] == letter:
            new[i] = letter
            
        elif new[i] != '*':
            new[i] = new[i]

        else:
           new[i] = format_word[i]

    quant = 0 
    palavra_final = ''
    for a in new:
        
        if a != '*':
            quant +=1

    for i in new:
        palavra_final += i

    if quant == len(secret_word):
        fim_excucao = True
        print("letras que já foram acertadas: " + palavra_final)
        print('Parabens vc completou a palavra com sucesso!!!!')








