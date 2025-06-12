lista=['oi' , 'tchau', 'ola']
#-----------------------------------------
print(lista[1])
#------------------------------------------
lista[2]= 'adeus'
print(lista)
#------------------------------------------
lista.append("ola")
print(lista)
#------------------------------------------
lista.insert(0, 'cachorro')
print(lista)
#------------------------------------------
lista.remove('adeus')
print(lista)
# -----------------------------------------
del lista[2]
print(lista)
#------------------------------------------
lista.pop(2)
print(lista)