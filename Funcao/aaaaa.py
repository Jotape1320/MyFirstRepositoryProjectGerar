"""1. Conversor de temperatura
Crie uma função chamada converter_temperatura()
que receba uma temperatura em Celsius e retorne o valor convertido para Fahrenheit
e Kelvin
Fórmula: 
Fahrenheit = Celsius × 1,8 + 32.
Kelvin = Celsius + 273.15
No programa principal, peça a temperatura ao usuário e mostre o resultado.
"""
def converterTemperatura(celsius):
    print (f"{celsius*1.8+32}")
    print (f"{celsius+273.15}")

#converterTemperatura(30)

"""2. Calculadora de viagem
Crie uma função chamada calcular_combustivel() que receba a distância de uma viagem, 
o consumo do veículo em km/L e o preço do litro do combustível.
A função deve calcular e retornar a quantidade de litros necessária para a viagem 
e o custo total estimado.
Exemplo:
- Distância: 300 km
- Consumo: 10 km/L
- Preço do litro: R$ 6,00
- Resultado: 30 litros e R$ 180,00."""

def calcularCombustivel(distancia,consumo,preco):
    totalLitro = distancia/consumo*preco
    print (f"{distancia/consumo} litros e R$ {totalLitro}")

#calcularCombustivel(520,8,5.60)

"""
4. Simulador de compra parcelada
Crie uma função chamada calcular_parcela() que receba o preço de um produto 
e a quantidade de parcelas desejada.
Regras:
- Pagamento à vista (1 parcela): desconto de 10%.
- De 2 a 3 parcelas: sem desconto ou acréscimo.
- Acima de 3 parcelas: acréscimo de 10% sobre o preço original.
A função deve retornar o valor de cada parcela.
"""
def calcularParcela(produto,parcela):
    if parcela == 1:
        print(f"O valor a ser pago vai ser de R${produto*0.9}")
    elif parcela >1 and parcela <=3:
        print(f"O valor a ser pago vai ser de R${produto}, Sem desconto")
    elif parcela >3:
        print(f"O valor a ser pago vai ser de R${produto*1.1}, 10% à mais")
    else:
        print(f"Valor informado é inválido, tente novamente")