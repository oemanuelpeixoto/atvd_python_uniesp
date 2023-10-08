def calcular_soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Digite um número inteiro positivo.")
else:
    soma_digitos = calcular_soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é: {soma_digitos}")
