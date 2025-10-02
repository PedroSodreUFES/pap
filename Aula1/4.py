a = input("Um número please brother: ")
if not a.isnumeric():
    print("Você não digitou um inteiro!")
    exit()

cont = 0
for x in a:
    cont += int(x)
print(cont)