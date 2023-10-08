import math

# Classe "Circulo"
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio**2

print("Classe Circulo:")
circulo = Circulo(5)
area = circulo.calcular_area()
print(f"A área do círculo é: {area}")

# Classe "Livro"
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

print("\nClasse Livro:")
livro = Livro("Dom Quixote", "Miguel de Cervantes")
detalhes_livro = livro.detalhes()
print(detalhes_livro)

# Classe "Retangulo"
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

print("\nClasse Retangulo:")
retangulo = Retangulo(4, 6)
area_retangulo = retangulo.calcular_area()
print(f"A área do retângulo é: {area_retangulo}")

# Classe "ContaBancaria"
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

print("\nClasse ContaBancaria:")

conta = ContaBancaria(1000, "João")
conta.depositar(500)
conta.sacar(300)
print(f"Saldo atual: {conta.saldo}")

# Classe "Pessoa"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"{self.nome} diz: Olá!")

print("\nClasse Pessoa:")
pessoa = Pessoa("Maria", 30)
pessoa.falar()

# Classe "Produto"
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

print("\nClasse Produto:")
produto = Produto("Notebook", 1200, 3)
total_produto = produto.calcular_total()
print(f"Total do produto: R${total_produto}")

# Classe "Carro"
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

print("\nClasse Carro:")
carro = Carro("Toyota", "Corolla", 2022)
detalhes_carro = carro.detalhes()
print(detalhes_carro)

# Classe "Aluno"
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

print("\nClasse Aluno:")
aluno = Aluno("Ana", [8, 9, 7])
media_notas = aluno.calcular_media()
print(f"A média das notas do aluno é: {media_notas}")

# Classe "Triangulo"
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

print("\nClasse Triangulo:")
triangulo = Triangulo(3, 4, 5)
perimetro = triangulo.calcular_perimetro()
print(f"O perímetro do triângulo é: {perimetro}")

# Classe "Funcionario"
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        self.salario += (self.salario * percentual / 100)

print("\nClasse Funcionario:")
funcionario = Funcionario("Carlos", 3000, "Analista")
funcionario.aumentar_salario(10)
print(f"Salário atualizado: R${funcionario.salario}")
