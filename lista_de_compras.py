def menu():
    print("Lista de Compras")
    print("-------------------------------")
    print("1- Adicionar item à lista ")
    print("2- Remover item da lista ")
    print("3- Exibir lista de compras")
    print("4- Sair")

def adicionar_item(lista):
    item = input("Digite o item que deseja adicionar: ")
    lista.append(item)
    print(f"{item} foi adicionado à lista.")

def remover_item(lista):
    item = input("Digite o item que deseja remover: ")
    if item in lista:
        lista.remove(item)
        print(f"{item} foi removido da lista.")
    else:
        print(f"{item} não está na lista.")

def mostrar_item(lista):
    if lista:
        print("Sua Lista de Compras: ")
        # enumerate itera a posição e o valor
        for x, item in enumerate(lista, 1):
            print(f"{x}. {item}")
    else:
        print(" Não há itens.")

def main(): 
    lista_compras = []

    while True:
        menu()
        opcao = input(" Escolha qual opção deseja realizar: ")
        print("-------------------------------")

        if opcao == "1":
            adicionar_item(lista_compras)
        elif opcao == "2":
            remover_item(lista_compras)
        elif opcao == "3":
            mostrar_item(lista_compras)
        elif opcao == "4":
            print("Até logo!")
            break  # Interrompe o loop
        else:
            print("Opção inválida, tente novamente.")



main()