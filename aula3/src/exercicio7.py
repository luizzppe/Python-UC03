def seq():
    termos=int(input("Defina o numeros de termos mostrados da sequência: "))
    numeros=[]
    a, b=0, 1
    while len(numeros) < termos:
        numeros.append(a)
        a,b = b, a+b
    print(numeros)
seq()