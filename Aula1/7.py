n = int(input("Digite um número: "))
if n >= 0:
    for x in range(n + 1):
        print(n - (x))
else:
    for x in range(-n + 1):
        print(n + (x))
print("FIM!")