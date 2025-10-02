matriz = []
for x in range(3):
    linha = []
    for y in range(3):
        linha.append(float(input("Digite um número: ")))
    matriz.append(linha)

for x in range(3):
    for y in range(x+1):
        aux = matriz[x][y]
        matriz[x][y] = matriz[y][x]
        matriz[y][x] = aux

for linha in matriz:
    print(linha)