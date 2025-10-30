def head(li):
    return li[0]

def tail(li):
    return li[1:]

def init(li):
    return li[:-1]

def last(li):
    return li[-1]

def fibonacci(index):
    if index == 0:
        return 0
    
    elif index == 1:
        return 1
    
    else:
        return fibonacci(index-1) + fibonacci(index-2)

def concatlist(li1, li2):
    if li1 == [] and li2 == []:
        return []
    elif (li1 == []):
        return concatlist(li2, [])
    else:
        return [head(li1)] + concatlist(tail(li1), li2)
    
def pertenceLista(x, li):
    if li == []:
        return False
    elif x == head(li):
        return True
    else:
        return pertenceLista(x, tail(li))
    
def maioresQue(n, li):
    if(li == []):
        return 0
    if(n < head(li)):
        return 1 + maioresQue(n, tail(li))
    else:
        return 0 + maioresQue(n, tail(li))

def listaDeMaiores(n, li):
    if(li == []):
        return []
    if n < head(li):
        return [head(li)] + listaDeMaiores(n, tail(li))
    else:
        return listaDeMaiores(n, tail(li))
    
def inverteLista(li):
    if li == []:
        return []
    else:
        return [last(li)] + inverteLista(init(li))
    
def palindromo(li):
        return li + inverteLista(li)

def tamanhoLista(li):
    if li == []:
        return 0
    else:
        return 1 + tamanhoLista(tail(li))

def ehPrimoFor(n, m):
    if(m == n):
        return True
    if n <= 1 or (n % m == 0 and (m != 1 and m != n)):
        return False
    else:
        return ehPrimoFor(n, m+1)
    
def ehPrimo(n):
    return ehPrimoFor(n, 2)

def strip(l1, l2):
    if l2 == []:
        return []
    if pertenceLista(head(l2), l1):
        return [head(l2)] + strip(l1, tail(l2))
    else:
        return strip(l1, tail(l2))

def consoantList(l1, l2):
    aux = []
    # cria uma lista só com as consoantes
    for letter in l1:
        if letter not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            aux.append(letter)
    
    # Realiza a verificação
    return aux == strip(aux, l2)

def matches(l1, l2):
    if l2 == []:
        return []
    if list(l1) == strip(list(l1), list(head(l2))):
        return [head(l2)] + matches(l1, tail(l2))
    else:
        return matches(l1, tail(l2))

def nextPrime(n):
    n = n+1
    if(ehPrimo(n)):
        return n
    else:
        return nextPrime(n)
    
def primes(number, divisor):
    if number == 1:
        return []
    if number % divisor == 0:
        return [divisor] + primes(number/divisor, divisor)
    else:
        return primes(number, divisor + 1)
