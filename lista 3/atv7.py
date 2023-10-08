def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")
