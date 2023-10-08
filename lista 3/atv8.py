def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Escolha a opção:\n1. Converter de Celsius para Fahrenheit\n2. Converter de Fahrenheit para Celsius\n")
temperatura = float(input("Digite a temperatura: "))

if opcao == "1":
    resultado = celsius_fahrenheit(temperatura)
    print(f"{temperatura}°C é igual a {resultado}°F.")
elif opcao == "2":
    resultado = fahrenheit_celsius(temperatura)
    print(f"{temperatura}°F é igual a {resultado}°C.")
else:
    print("Opção inválida.")
