def segundo_menor(vetor):
    if len(vetor) < 2:
        return None
    menor = segundo = float('inf')
    for numero in vetor:
        if numero < menor:
            segundo = menor
            menor = numero
        elif numero < segundo and numero != menor:
            segundo = numero
    return segundo

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90]
segundo_menor_numero = segundo_menor(vetor)
print("Segundo menor número:", segundo_menor_numero)
