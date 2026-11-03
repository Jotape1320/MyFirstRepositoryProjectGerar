"""1. Conversor de temperatura
Crie uma função chamada converter_temperatura()
que receba uma temperatura em Celsius e retorne o valor convertido para Fahrenheit
e Kelvin
Fórmula: 
Fahrenheit = Celsius × 1,8 + 32.
Kelvin = Celsius + 273.15
No programa principal, peça a temperatura ao usuário e mostre o resultado.
"""
def ConverterTemperatura(celsius):
    print (f"{celsius*1.8+32}")
    print (f"{celsius+273.15}")

ConverterTemperatura(30)