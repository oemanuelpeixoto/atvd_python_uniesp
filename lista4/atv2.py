def ordenar_vetor(vetor, ordem="crescente"):
    if ordem == "crescente":
        return sorted(vetor)
    elif ordem == "decrescente":
        return sorted(vetor, reverse=True)
    else:
        return "Ordem inválida"

# Exemplo de uso:
vetor = [64, 34, 25, 12, 22, 11, 90]
ordenado_crescente = ordenar_vetor(vetor, "crescente")
ordenado_decrescente = ordenar_vetor(vetor, "decrescente")
print("Vetor ordenado crescente:", ordenado_crescente)
print("Vetor ordenado decrescente:", ordenado_decrescente)
