def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
if n <= 0:
    print("Digite um número inteiro positivo.")
else:
    resultado = fibonacci(n)
    print(f"Sequência de Fibonacci com {n} termos: {resultado}")
