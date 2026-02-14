# Encontrar valores que aparecem em ambas as listas

# Listas originais
lista1 = [1, 2, 3, 4, 5, 5]
lista2 = [3, 4, 5, 6, 7, 7]

# Método 1: Usando operador & com conjuntos (mais conciso)
intersecao_1 = list(set(lista1) & set(lista2))

# Método 2: Usando list comprehension
intersecao_2 = list(dict.fromkeys([x for x in lista1 if x in lista2]))

# Método 3: Usando filter e set
set2 = set(lista2)
intersecao_3 = list(dict.fromkeys(filter(lambda x: x in set2, lista1)))

# Exibir resultados
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"\nInterseção (método 1 - conjuntos): {sorted(intersecao_1)}")
print(f"Interseção (método 2 - list comprehension): {intersecao_2}")
print(f"Interseção (método 3 - filter): {intersecao_3}")
