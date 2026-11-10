#crie uma lista com alguns produtos
produtos = ["mouse", "teclado", "monitor"]

#acessando elementos pelo indíce
#lembre-se: o primeiro elemento está no indice 0
print(f"{produtos}")

#adicionando elementos
#apeend(): adiciona um elemento ao final da lista

produtos.append("Headset")

#insert(): adiciona um elemento em uma posicao especifica, empurrando as demais para a frente
produtos.insert(1, "Webcam")

print(produtos[4])

#removendo elementos
#remove(): remove um elemento pelo seu valor
produtos.remove("mouse")

#pop(): remove um elemento pelo seu indice
produtos.pop(1)

#alterando elementos
#altera o valor de um elemento utilizando seu indice
produtos[0] = "Teclado Gamer"

#consultando a lista
#len(): retorna a quantidade de elementos na lista
print("Quantidade de produtos:", len(produtos)) #4

#in: verifica se determinado elemento existe
if"monitor" in produtos:
    print(f"Monitor existe na lista!")

#for: percorre todos os elementos da lista
print("\n=== LISTA DE PRODUTOS ===")

for produto in produtos:
    print(produto)