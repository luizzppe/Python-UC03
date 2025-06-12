import random

lista=['maca' , 'babana' , 'uva' , 'melancia' , 'limao']
# for frutas in range(5):
#     valor=input(f"Informe a {frutas+1}° fruta: ")
#     lista.append(valor)
def gerar_dados(qtd, valormin,valormax):
    return [random.randint(valormin, valormax) for _ in range (qtd)]

listavazia= list(lista)
sete=set(lista)
dic=dict[lista]
tupla=tuple(lista)
dic={j:valor for j, valor in enumerate(lista)}


print(f'Lista{listavazia}')
print(f'Set {sete}')
print(f'Dicionario {dic}')
print(f'Tupla {tupla}')
gerar_dados(8, 1, 50)