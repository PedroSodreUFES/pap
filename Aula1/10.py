n = int(input("Digite um número: "))
m = int(input("Digite um número: "))

menor = None
maior = None

if n < m:
    menor = n
    maior = m
else:
    menor = m
    maior = n

countPrimos = 0
for x in range(menor, maior + 1):
    contDivisor = 0
    for y in range(1, x+1):
        if x % y == 0:
            contDivisor+=1
    if contDivisor == 2:
        countPrimos += 1
        print(f"{y} é primo!")
    
print(countPrimos)