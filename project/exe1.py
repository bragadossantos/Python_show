# Remover valores repetidos mantendo a ordem original

# Lista original com valores repetidos
li = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Método 1: Usando dict.fromkeys() - mais conciso
li_sem_repetidos_1 = list(dict.fromkeys(li))

# Método 2: Usando um conjunto para rastrear elementos vistos
seen = set()
li_sem_repetidos_2 = []
for num in li:
    if num not in seen:
        seen.add(num)
        li_sem_repetidos_2.append(num)

# Exibir resultados
print(f"Lista original: {li}")
print(f"Sem repetidos (método 1): {li_sem_repetidos_1}")
print(f"Sem repetidos (método 2): {li_sem_repetidos_2}")