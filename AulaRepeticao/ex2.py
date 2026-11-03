print("Hi, EX2")

senha = "01234"

senhalogin = str (input("Digite a senha: \n"))

while senhalogin != senha:
    senhalogin = str (input("Digite a senha novamente: \n"))
print()

print ("Senha Correta! \n")

"""Ou assim:"""

while True:
    senhalogin = str(input("Digite a senha: "))
    if senhalogin == senha:
        break
    else:
        print("Senha Incorreta!")

print ("Senha Correta!")
       
print (":)")