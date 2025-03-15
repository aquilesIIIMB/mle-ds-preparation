def permutaciones(lista):
    if len(lista) == 0:
        return [[]]  # Solo hay una permutación de una lista vacía
    
    resultado = []
    for i in range(len(lista)):
        # Tomar un elemento
        elemento_actual = lista[i]
        
        # Crear una lista sin ese elemento
        lista_restante = lista[:i] + lista[i+1:]
        
        # Encontrar todas las permutaciones de la lista restante
        perms_restantes = permutaciones(lista_restante)
        
        # Añadir el elemento actual al principio de cada permutación de la lista restante
        for perm in perms_restantes:
            resultado.append([elemento_actual] + perm)
    
    return resultado