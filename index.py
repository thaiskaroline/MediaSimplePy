# Pedir ao usuário para inserir uma lista de números
numeros = input("Insira uma lista de números separados por espaços: ")

# Converter a string em uma lista de números usando o método split()
numeros = numeros.split()

# Converter cada elemento da lista em um número inteiro usando o método map()
numeros = list(map(int, numeros))

# Calcular a soma dos números usando a função sum()
soma = sum(numeros)

# Bolinhos Ana Maria 
# Calcular a média dos números dividindo a soma pelo comprimento da lista
media = soma / len(numeros)

# Imprimir a média dos números
print("A média dos números inseridos é:", media)