lista = []
for a in range(5):
    n = float(input("Digite um número: "))
    lista.append(n)

for x in range(5):
    for y in range(5):
        if(lista[x] < lista[y]):
            aux = lista[x]
            lista[x] = lista[y]
            lista[y] = aux

print(lista)