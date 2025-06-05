tamanho=int(input("Informe o tamanho: "))
def parteum(tamanho):
    for _ in range(tamanho):
        print("*" * tamanho)
# parteum(tamanho)

def partedois(tamanho):
    meio=tamanho // 2
    for i in range(tamanho):
        linha=""
        for j in range(tamanho):
            if i == meio and j == meio:        
                linha += " "
            else:
                linha+= "*"
        print(linha)
# partedois(tamanho)

def partetres(tamanho):
    altura = tamanho // 2
    for i in range(altura+1):
        espacos = " " * (altura-i)
        asteristicos = "*" * (2*i+1)
        print(espacos + asteristicos + espacos)

partetres(tamanho)