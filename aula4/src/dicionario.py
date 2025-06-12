dicionario = {
    'Nome' : 'Luiz',
    'Idade' : '18',
    'Sobrenome' : 'Plantz'
    }
print(dicionario)
#-------------------------------------------
dicionario2={'Trabalho' : 'Programador'}
dicionario.update(dicionario2)
print(dicionario)
#-------------------------------------------
dicionario['Nome'] = 'luizz'
print(dicionario)
#-------------------------------------------
del dicionario['Sobrenome']
print(dicionario)