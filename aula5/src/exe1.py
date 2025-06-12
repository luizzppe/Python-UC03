# def criar_arquivo(nome_arquivo: str, conteudo: str):
#     """Cria um arquivo com o nome e contudo fornecidos."""
#     with open(nome_arquivo, 'w') as arquivo:
#         arquivo.write(conteudo)
#         print("Arquivo criado com sucesso")
# nome = input("Digite  nome do arquivo: ")
# criar_arquivo(f'./aula5/arquivos/{nome}.txt','Este e um exemplo de arquivo criado com python')


# def ler_arquivo(nome_arquivo: str) -> str:
#     with open(nome_arquivo, 'r') as arquivo:
#         return arquivo.read()
# nome = input("Digite nome do arquivo: ")
# print(ler_arquivo(f'./aula5/arquivos/{nome}.txt'))


# def adicionar_conteudo(nome_arquivo: str, conteudo: str):
#      """Adiciona um conteudo ao arquivo desejado."""
#      with open(nome_arquivo, 'a') as arquivo:
#          arquivo.write('\n' + conteudo)
#          print("Arquivo editado com sucesso!")
# nome = input('Informe o nome do arquivo: ')
# conteudo=input("Digite um texto a ser adicionado: ")
# adicionar_conteudo(f'./aula5/arquivos/{nome}.txt' , conteudo)

# import os
# def deletar_arquivo(nome_arquivo: str):
#     """Exclui um arquivo se existir"""
#     if os.path.exists(nome_arquivo):
#         os.remove(nome_arquivo)
#         print('Arquivo removido com sucesso')
#     else:
#         print("Arquivo não encontrado")
# nome = input('Informe o nome do arquivo que deseja remover: ')
# deletar_arquivo(f'./aula5/arquivos/{nome}.txt')


# def contar_linhas(nome_arquivo: str) -> int:
#     """Retorna a quantidade de linhas de um arquivo"""
#     with open(nome_arquivo, 'r') as arquivo:
#         return len(arquivo.readlines()) 
    
# nome = input("Insira o nome do arquivo que deseja contar as linhas: ")
# print(contar_linhas(f'./aula5/arquivos/{nome}.txt'))


# def verifica_palavra(nome_arquivo: str, palavra) -> bool:
#     """Retorna a verificação de uma palavra em um arquivo"""
#     with open (nome_arquivo, 'r') as arquivo:
#         return palavra in arquivo.read() 

# nome = input("Insira o nome do arquivo que deseja verificar a palavra: ")
# print(verifica_palavra(f'./aula5/arquivos/{nome}.txt', ' '))


# def soma_num(nome_arquivo: str) -> int:
#     """Soma os numeros de um arquivo"""
#     with open(nome_arquivo, 'r') as arquivo:
#         return sum(int(linha.strip()) for linha in arquivo)
# nome = input("Insira o nome do arquivo que deseja verificar a palavra: ")   
# print(soma_num(f'./aula5/arquivos/{nome}.txt'))

import os
def atualiza_linha(nome_arquivo: str, novo_conteudo: str, linha_alvo: int):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        if 0 <= linha_alvo < len(linhas):
            linhas[linha_alvo] = novo_conteudo + '\n'
    with open(nome_arquivo, 'w') as arq:
        arq.writelines(linhas)
        print(linhas)
nome = input("Insira o nome do arquivo que deseja verificar a palavra: ")   
conteudo = input("Insira o conteudo: ") 
linha = int(input("Insira o numero da linha desejada: ")) 
print(atualiza_linha(f'./aula5/arquivos/{nome}.txt'), conteudo, linha)
      