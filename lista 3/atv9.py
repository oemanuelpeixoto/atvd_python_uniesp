def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b

print("Escolha uma operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão")
opcao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = somar(num1, num2)
elif opcao == "2":
    resultado = subtrair(num1, num2)
elif opcao == "3":
    resultado = multiplicar(num1, num2)
elif opcao == "4":
    resultado = dividir(num1, num2)
else:
    resultado = "Opção inválida."

print(f"Resultado: {resultado}")
