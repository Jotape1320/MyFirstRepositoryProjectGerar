"""Peça o nome do aluno e logo em seguida receba 3 ou mais notas, calcule a média e informe a situação do aluno:

Se media for menor que 5 aluno está reprovado
Se for de 5 e menor que 7 está em recuperação
igual maior que 7 aluno está aprovado"""

nome = str(input ("Nome do Aluno: \n"))

nota1 = float(input ("Nota do 1° Bimestre: \n"))

nota2 = float(input ("Nota do 2° Bimestre: \n"))

nota3 = float(input ("Nota do 3° Bimestre: \n"))

media = (nota1+nota2+nota3)/3

if media<5:
    print (f"O aluno {nome} foi reprovado com a notinha {media:.2f} \n")
elif media>=5 and media<7:
    print (f"O aluno {nome} ficou de recuperação com a notinha {media:.2f} \n")
elif  media >=7:
    print (f"O aluno {nome} foi aprovado com a notinha {media:.2f} \n")

print("FIM \n")

print(":)")