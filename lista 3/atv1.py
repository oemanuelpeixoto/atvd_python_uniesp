def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)
resultado = verificar_aprovacao(media)

print(f"A média do aluno é: {media}")
print(f"O aluno está {resultado}.")
