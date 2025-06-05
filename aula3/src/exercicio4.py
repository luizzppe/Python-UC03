import time
nt=int(input("Insira o número da tabuada: "))
def tabuada(nt):
    for i in range(0,11):
        print(f"{i} x {nt} = {i*nt}")
        time.sleep(1)
tabuada(nt)