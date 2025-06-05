n1=int(input("Primeiro número: "))
n2=int(input("Segundo número: "))
def imprimir(n1,n2):
    for numeros in range(n1,n2+1):
        print(f"{numeros}")

imprimir(n1,n2)