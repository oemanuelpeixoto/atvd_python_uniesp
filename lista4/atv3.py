def encontrar_max_min(vetor):
    if not vetor:
        return None, None
    max_element = min_element = vetor[0]
    for elemento in vetor:
        if elemento > max_element:
            max_element = elemento
        if elemento < min_element:
            min_element = elemento
    return max_element, min_element

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90]
maximo, minimo = encontrar_max_min(vetor)
print("Elemento máximo:", maximo)
print("Elemento mínimo:", minimo)
