def contar_pares_impares(vetor):
    vetor_ordenado = sorted(vetor, reverse=True)
    pares = sum(1 for num in vetor_ordenado if num % 2 == 0)
    impares = sum(1 for num in vetor_ordenado if num % 2 != 0)
    return pares, impares

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90]
pares, impares = contar_pares_impares(vetor)
print("Vetor ordenado em ordem decrescente:", vetor)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
