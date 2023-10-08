#Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário


maximo = int(input("Digite um valor máximo para a sequência de Fibonacci: "))

a, b = 0, 1

while a <= maximo:
    print(a, end=" ")
    a, b = b, a + b
