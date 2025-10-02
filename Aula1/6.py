lista = []
for a in range(10):
    n = float(input("Digite um número: "))
    lista.append(n)

menor = None
maior = None
for x in range(10):
    if  menor == None or lista[x] < menor:
        menor = lista[x]
    if  maior == None or lista[x] > maior:
        maior = lista[x]
print(f"Menor: {menor}\nMaior: {maior}")