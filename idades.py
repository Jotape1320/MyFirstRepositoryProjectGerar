"""Crie um programa que solicite o nome e a idade de uma pessoa.
 Depois, classifique-a como Criança, Adolescente ou Adulto,
de acordo com a idade, e exiba todas as informações
de forma organizada."""

nome = str( input("Seu Nome:  \n"))



idade = int(input("Sua Idade:  \n"))

print()

if idade<=12:
    print (f"Você se chama {nome} tem {idade} anos e você é uma Criança \n")
elif idade>=13 and idade<18:
    print (f"Você se chama {nome} tem {idade} anos e você é um Adolescente \n")
elif idade>=18:
    print (f"Você se chama {nome} tem {idade} anos e você é um Adulto\n")

print("FIM")

print(":) \n")
