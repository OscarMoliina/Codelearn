import itertools

def read(lst:tuple,s:str):
    n = len(lst)
    d = {}
    for i in range(n):
        d[chr(65+i)] = lst[i]
    return eval(s,d)

def taula(n, frase):
    l = [True, False]
    lst = list(itertools.product(l, repeat=n))
    result = []
    for i in lst:
        result.append(read(i,frase))
    return result

n     = int(input("Ingrese la cantidad de variables: "))
frase = input('Ingrese la función booleana: ')
print(taula(n,frase))