#Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
#programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
#computador e determinar o vencedor.

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

print("Escolha uma opção:")
for i, opcao in enumerate(opcoes, 1):
    print(f"{i}. {opcao}")

escolha_usuario = int(input("Digite o número da sua escolha: ")) - 1

escolha_computador = random.randint(0, 2)

print(f"Você escolheu: {opcoes[escolha_usuario]}")
print(f"O computador escolheu: {opcoes[escolha_computador]}")

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario - escolha_computador) % 3 == 1:
    print("Você ganhou!")
else:
    print("O computador ganhou!")
