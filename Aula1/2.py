word = input("Digite uma palavra: ")
cont = 0
for a in word:
    if(a in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
        cont+=1
print(f"O número de vogais é {cont}")