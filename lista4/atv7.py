def terceiro_maior(vetor):
    vetor = list(set(vetor))
    if len(vetor) < 3:
        return None
    vetor.sort(reverse=True)
    return vetor[2]

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90, 90, 34, 11]
terceiro_maior_numero = terceiro_maior(vetor)
print("Terceiro maior número:", terceiro_maior_numero)
