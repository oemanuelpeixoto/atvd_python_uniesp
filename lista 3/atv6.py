def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    count = 0
    for char in texto:
        if char in vogais:
            count += 1
    return count

texto = input("Digite uma frase: ")
qtd_vogais = contar_vogais(texto)
print(f"A frase contém {qtd_vogais} vogais.")
