import re

def palindrome(texto):
    texto = re.sub(r'[^a-zA-Z]', '', texto.lower())
    return texto == texto[::-1]

texto = input("Digite uma palavra ou frase: ")
if palindrome(texto):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
