vezes=0
opcao=""
menu = ("1. carrinho, 2. lista de produtos, 3. Sair")
def menuu(vezes,opcao,menu):
    while opcao != "3": 
        print(menu)

        opcao= input("Digite opção desejada: ")

        if opcao == "1":
            print("Carrinho: Bermuda, camisa, casaco")
            vezes+=1
        elif opcao == "2":
            print("Bermuda, tenis, camisa, casaco")
            vezes+=1
        elif opcao == "3":
            print("Saindo!")
        
    else:
        print(f"Voçê intergiu com o menu {vezes} vezes")
menuu(vezes,opcao,menu)