def remover_duplicatas(vetor):
    return list(set(vetor))

# Exemplo de uso:
vetor = [1, 2, 2, 3, 4, 4, 5, 5]
vetor_sem_duplicatas = remover_duplicatas(vetor)
print("Vetor sem duplicatas:", vetor_sem_duplicatas)
