#Faça um programa que leia uma lista de números e retorne a média dos números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_pares = 0
contador_pares = 0


for numero in numeros:

    if numero % 2 == 0:
        soma_pares += numero  
        contador_pares += 1  


if contador_pares > 0:
    media_pares = soma_pares / contador_pares
    print(f"A média dos números pares é: {media_pares}")
else:
    print("Não há números pares na lista.")
