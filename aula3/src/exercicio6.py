palavra=str(input("Digite a palavra: "))
palindromo=str(input("Digite o palindromo: "))

def verifica_palindromo(palavra,palindromo):
    if palavra == palindromo[::-1]:
        return True
    else:
        return False
    
verifica_palindromo(palavra,palindromo)