"""1. Listas — Lista de compras
Crie um programa que permita organizar uma lista de compras.
O programa deve: 
    Criar uma lista vazia chamada compras.
    Adicionar 3 produtos utilizando append().
    Adicionar mais um produto na segunda posição utilizando insert().
    Exibir todos os produtos utilizando for.
    Remover um produto utilizando remove().
    Exibir todos os produtos utilizando for.
    Mostrar quantos produtos existem na lista utilizando len()."""

compras = []

compras.append("Arroz")
compras.append("Feijão")
compras.append("Carne moída")

compras.insert(1, "alho")

for compra in compras:
    print(compra)

print()

compras.remove("Feijão")

for compra in compras:
    print(compra)

print()

print(f"Produtos na lista:", len(compras))