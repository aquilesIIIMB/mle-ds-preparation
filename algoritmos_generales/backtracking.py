def backtrack(estado_actual, otras_variables):
    # 1. Verificar condición de terminación
    if condicion_terminacion:
        resultado.append(solucion_actual)
        return
    
    # 2. Explorar todas las opciones posibles
    for opcion in opciones_disponibles:
        # 3. Aplicar la opción actual
        aplicar_opcion(opcion)
        
        # 4. Llamada recursiva con el nuevo estado
        backtrack(nuevo_estado, otras_variables)
        
        # 5. Deshacer la opción (opcional, en algunos casos)
        deshacer_opcion(opcion)

"""
Marco de trabajo para resolver problemas de backtracking
Cuando te enfrentes a un problema que pueda utilizar backtracking, aplica este marco:

Preparación:

Define las estructuras de datos necesarias
Establece el mapeo o reglas del problema

Llamar la funcion inicial de backtracking

Invocación inicial:

Llama a backtrack con los valores iniciales
Retorna el resultado acumulado


Estrategia general para resolver problemas de backtracking
Para enfrentar problemas similares, es útil seguir estos pasos:

Identificar el espacio de búsqueda: ¿Qué conjunto de elementos estamos explorando?
Definir el estado: ¿Cómo representamos el progreso de nuestra solución?
Definir las decisiones: ¿Qué opciones tenemos en cada paso?
Establecer condiciones de terminación: ¿Cuándo añadimos una solución al resultado?
Implementar la función de backtracking: Una función recursiva que explora todas las posibilidades.

Problemas similares
Los siguientes problemas comparten características y enfoques similares:

Generación de permutaciones: Por ejemplo, generar todas las permutaciones de una lista de números.
Generación de subconjuntos: Encontrar todos los posibles subconjuntos de un conjunto dado.
Problemas de enumeración combinatoria: Como generar todas las palabras posibles con ciertas restricciones.
Word Search: Encontrar palabras específicas en una matriz de caracteres.
N-Queens: Colocar N reinas en un tablero N×N sin que se ataquen entre sí.
"""

""" Combinacion
def letterCombinations(digits):
    # Caso base: si no hay dígitos, retornamos una lista vacía
    if not digits:
        return []
    
    # Definimos el mapeo de dígitos a letras según el teclado telefónico
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    result = []  # Lista para almacenar todas las combinaciones
    
    def backtrack(index, current_string):
        # Condición de parada: si hemos procesado todos los dígitos
        if len(current_string) == len(digits):
            result.append(current_string)  # Añadimos la combinación completa al resultado
            return
        
        # Obtenemos el dígito actual y sus letras correspondientes
        current_digit = digits[index]
        letters = phone_map[current_digit]
        
        # Exploramos todas las letras posibles para este dígito
        for letter in letters:
            # Avanzamos recursivamente al siguiente dígito, añadiendo la letra actual
            backtrack(index + 1, current_string + letter)
    
    # Iniciamos el backtracking desde el primer dígito con una cadena vacía
    backtrack(0, "")
    
    return result
"""
