# Solicita um número ao usuário
numero = int(input("Digite um número inteiro positivo maior que 1: "))

if numero <= 1:
    print("Por favor, digite um número inteiro positivo maior que 1.")
else:
    divisores = 0

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            divisores += 1
            break  # 
    if divisores == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
