#Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.
nomes = ["Ana", "João", "Alice", "Pedro", "Amanda", "Mariana", "Alberto"]

nomes_com_a = []

for nome in nomes:
    if nome.upper().startswith('A'):
        nomes_com_a.append(nome)

print("Nomes que começam com 'A' (maiúscula):")
for nome in nomes_com_a:
    print(nome)