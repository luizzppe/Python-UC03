import time

n=int(input("Digite o número para a contagem regressiva: "))

def contagem_regressiva(n):
    while True: 
        n >= 0
        print(f"{n}")
        time.sleep(1)
        n -= 1
        if n == -1:
            break
contagem_regressiva(n) 