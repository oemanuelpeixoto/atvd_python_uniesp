def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    meio = len(vetor_ordenado) // 2
    if len(vetor_ordenado) % 2 == 0:
        return (vetor_ordenado[meio - 1] + vetor_ordenado[meio]) / 2
    else:
        return vetor_ordenado[meio]

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90]
mediana_valor = mediana(vetor)
print("Mediana:", mediana_valor)
