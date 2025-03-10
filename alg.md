🔍 Example 1: Binary Search

In binary search, you’re looking for a target value in a sorted array by repeatedly halving the search space.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found target
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half
    
    return -1  # Not found


🔍 Example 2: Balanced Binary Search Tree (BST)

When searching or inserting an element in a balanced binary search tree, the search space halves at each level.

def search_bst(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)


🔍 Example 1: Merge Sort

Merge sort is a classic example of an O(N log N) algorithm.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


🔍 Example 2: Heap Sort

Heap sort involves building a binary heap and repeatedly extracting the maximum/minimum element.

Steps:
	1.	Build a max heap in O(N) time.
	2.	Extract the maximum element (root) and heapify in O(log N) time.
	3.	Repeat this N times.

The overall complexity is O(N log N).



🔍 Example 3: Quick Sort (Average Case)

Quick sort uses a divide-and-conquer approach similar to merge sort:
	•	Divide: Pick a pivot, partition the array into two subarrays.
	•	Conquer: Recursively sort each subarray.

The average case complexity is O(N log N).


def find_min_in_rotated_sorted_array(arr):
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return arr[low]


🔍 Problem 1: Two Sum (Easy)

Prompt: Given an array of integers and a target, find two numbers that add up to the target.

def two_sum(arr, target):
    hash_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i


🔍 Problem 2: Merge Two Sorted Arrays (O(N + M))

Prompt: Merge two sorted arrays into one sorted array.

def merge_arrays(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


🔍 Problem 5: Find Duplicates in an Array (O(N))

Prompt: Find if any duplicates exist in the array.

Solution Using Hash Set:

def contains_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

🔍 Step 6: Precompute Results to Avoid Repeated Work

If your algorithm does repeated calculations, try memoization or precomputation.

Example: Fibonacci Sequence (Naive vs. Optimized)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


📚 Tipos de Datos y Estructuras: Arrays, Strings, Hash Tables, Stacks, Queues, Trees y Graphs

🔍 1. Arrays (Arreglos)

Descripción:
	•	Una colección de elementos contiguos en memoria.
	•	Cada elemento se accede usando un índice (index).

arr = [1, 2, 3, 4, 5]
print(arr[2])  # Output: 3 (accede al índice 2)

Características:
	•	Acceso: O(1) (tiempo constante) para acceder a cualquier elemento.
	•	Inserción/Eliminación: O(N) en el peor caso, si implica mover elementos.

🔍 2. Strings

Descripción:
	•	Un array de caracteres en el que cada carácter ocupa una posición indexada.

s = "hello"
print(s[1])  # Output: 'e'

Características:
	•	Inmutables: En la mayoría de los lenguajes, no puedes cambiar un carácter de una string directamente.
	•	Acceso: O(1) para acceder a un carácter específico.
	•	Concatenación: O(N) debido a la creación de una nueva string.


🔍 3. Hash Tables

Descripción:
	•	Una estructura de datos que almacena pares clave-valor, con acceso rápido.
	•	Internamente, usa una función hash para calcular el índice de almacenamiento.

hash_table = {"a": 1, "b": 2, "c": 3}
print(hash_table["b"])  # Output: 2

Características:
	•	Acceso/Inserción/Eliminación: O(1) en promedio.
	•	Problemas: Colisiones (cuando dos claves tienen el mismo hash).


🔍 4. Stacks (Pilas)

Descripción:
	•	Una colección de elementos LIFO (Last In, First Out).
	•	El último elemento en entrar es el primero en salir.

stack = []
stack.append(1)  # Push
stack.append(2)
print(stack.pop())  # Output: 2 (Pop el último elemento)

Operaciones:
	•	push(x): Inserta un elemento en la pila.
	•	pop(): Elimina y devuelve el último elemento.
	•	peek(): Devuelve el elemento superior sin eliminarlo.

🔍 5. Queues (Colas)

Descripción:
	•	Una colección de elementos FIFO (First In, First Out).
	•	El primer elemento en entrar es el primero en salir.

from collections import deque

queue = deque([1, 2, 3])
queue.append(4)  # Añadir al final
print(queue.popleft())  # Output: 1 (Elimina el primer elemento)

Operaciones:
	•	enqueue(x): Inserta un elemento al final.
	•	dequeue(): Elimina el primer elemento.
	•	peek(): Devuelve el primer elemento sin eliminarlo.


🔍 6. Trees (Árboles)

Descripción:
	•	Una estructura jerárquica con un nodo raíz y varios nodos hijos.
	•	El árbol binario es el más común, donde cada nodo tiene a lo sumo dos hijos.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

Tipos comunes:
	•	Árbol binario: Cada nodo tiene a lo sumo dos hijos.
	•	Árbol de búsqueda binaria (BST): Los nodos a la izquierda son menores, y los nodos a la derecha son mayores.


🔍 7. Graphs (Grafos)

Descripción:
	•	Una colección de nodos y aristas que los conectan.
	•	Los grafos pueden ser dirigidos o no dirigidos.

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

Tipos comunes:
	•	No dirigido: Las conexiones no tienen dirección.
	•	Dirigido: Las conexiones tienen una dirección.
	•	Con peso: Las aristas tienen valores asociados.


------------

Apreciado Aki, a continuación te presento una serie de problemas clásicos de programación que suelen encontrarse en plataformas como LeetCode y HackerRank. Cada uno incluye una breve explicación, la propuesta de solución en Python y un análisis de complejidad. El objetivo es demostrar buenas prácticas de codificación y un entendimiento profundo de las estructuras de datos y algoritmos implicados.

1. Problemas comunes con Arrays

1.1 Two Sum

Enunciado: Dado un arreglo de enteros nums y un valor objetivo target, encuentra dos números en nums que sumen target. Devuelve los índices de esos dos números, o None si no existe una solución.

Análisis
	•	Solución ingenua (Fuerza Bruta):
	•	Recorremos todos los pares posibles hasta encontrar el que sume target.
	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼.
	•	Solución optimizada (Hash Map):
	•	Utilizamos un diccionario para guardar el valor y su índice.
	•	Por cada número num, calculamos complemento = target - num.
	•	Revisamos si complemento está en el diccionario. Si está, devolvemos los índices.
	•	Si no está, guardamos num en el diccionario con su índice.
	•	Complejidad temporal: ￼.
	•	Complejidad espacial: ￼ en el peor caso.

Implementación en Python

def two_sum(nums, target):
    """
    Retorna los índices de dos números en nums que suman el valor target.
    Si no existe, retorna None.
    """
    hash_map = {}  # Valor -> Índice
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in hash_map:
            return [hash_map[complemento], i]
        hash_map[num] = i
    return None

# Ejemplo de uso
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # [0, 1]

1.2 Maximum Subarray (Kadane’s Algorithm)

Enunciado: Dado un arreglo de números (que pueden ser positivos o negativos), encuentra el subarreglo contiguo con la suma más grande.

Análisis (Algoritmo de Kadane)
	1.	Mantén un acumulado current_sum que se reinicia a 0 en caso de volverse negativo.
	2.	Mantén una variable max_sum para registrar la mayor suma encontrada.
	3.	Al final, max_sum será la suma máxima de un subarreglo contiguo.

	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼.

Implementación en Python

def max_subarray(nums):
    """
    Retorna la máxima suma de un subarreglo contiguo.
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

# Ejemplo de uso
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))  # 6 (subarreglo [4, -1, 2, 1])

2. Problemas comunes con Strings

2.1 Reversar una String

Enunciado: Dada la cadena "hello", retorna "olleh".

Análisis
	•	Las cadenas en Python son inmutables, pero podemos obtener la versión invertida fácilmente usando slicing ([::-1]).
	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼ para la nueva cadena.

Implementación en Python

def reverse_string(s):
    """
    Retorna la cadena invertida.
    """
    return s[::-1]

# Ejemplo de uso
if __name__ == "__main__":
    original = "hello"
    print(reverse_string(original))  # "olleh"

2.2 Verificar si una String es Palíndromo

Enunciado: Verificar si una cadena es igual al leerla de izquierda a derecha y de derecha a izquierda.

Análisis
	•	Un palíndromo se lee igual en ambos sentidos.
	•	Se puede comparar la string original con su reverso.
	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼ o ￼ si solo comparamos índices (sin crear copia).

Implementación en Python

def is_palindrome(s):
    """
    Retorna True si 's' es un palíndromo, False en caso contrario.
    """
    return s == s[::-1]

# Ejemplo de uso
if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False

3. Problemas comunes con Hash Tables

3.1 Two Sum Optimizado

Este problema es esencialmente el mismo que el de Arrays → Two Sum. La aproximación usando un diccionario (hash map) es la más eficiente. Ya presentamos la solución en 1.1.

3.2 Anagramas

Enunciado: Dados dos strings, determinar si son anagramas (es decir, si tienen los mismos caracteres con las mismas frecuencias).

Análisis
	•	Se puede ordenar cada string y compararlos, obteniendo una complejidad de ￼.
	•	Alternativamente, se utiliza un contador de caracteres (collections.Counter) para comparar frecuencias en ￼.

Implementación en Python (usando Counter)

from collections import Counter

def are_anagrams(s1, s2):
    """
    Retorna True si s1 y s2 son anagramas, False de lo contrario.
    """
    return Counter(s1) == Counter(s2)

# Ejemplo de uso
if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))  # True
    print(are_anagrams("hello", "world"))    # False

4. Problemas comunes con Stacks

4.1 Balanceo de Paréntesis

Enunciado: Verificar si una expresión que incluye los caracteres (, ), {, }, [, ] está correctamente balanceada.

Análisis
	1.	Se usa una pila.
	2.	Cuando encontramos un símbolo de apertura, lo empujamos a la pila.
	3.	Cuando encontramos un símbolo de cierre, revisamos si la pila no está vacía y si el tope corresponde a la apertura adecuada.
	4.	Al final, si la pila queda vacía, la expresión está balanceada.

	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼ en el peor caso (todos son aperturas).

Implementación en Python

def is_valid_parentheses(s):
    """
    Retorna True si los paréntesis en la cadena 's' están balanceados.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Es un símbolo de cierre
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Es un símbolo de apertura
            stack.append(char)
    
    return len(stack) == 0

# Ejemplo de uso
if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))  # True
    print(is_valid_parentheses("([)]"))    # False

4.2 Evaluación de Expresiones Postfijas

Enunciado: Dada una expresión en notación postfija (por ejemplo: ["2", "1", "+", "3", "*"] que representa (2 + 1) * 3), evaluarla y devolver el resultado.

Análisis
	•	Se usa una pila.
	•	Al ver un número, se apila.
	•	Al ver un operador, se desapilan los dos últimos números, se aplica el operador y se apila el resultado.
	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼.

Implementación en Python

def eval_rpn(tokens):
    """
    Evalúa una expresión aritmética en notación postfija.
    """
    stack = []
    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncar hacia 0
                stack.append(int(a / b))
    return stack.pop()

# Ejemplo de uso
if __name__ == "__main__":
    expression = ["2", "1", "+", "3", "*"]  # (2+1)*3
    print(eval_rpn(expression))  # 9

5. Problemas comunes con Queues

5.1 Implementar un Sistema de Espera

Enunciado: Procesar clientes en orden FIFO (First In, First Out).

Análisis
	•	Se utiliza una cola para simular el flujo de clientes.
	•	En Python, es común usar collections.deque para operaciones eficientes de inserción y extracción al inicio.

Implementación en Python

from collections import deque

def simulate_queue(customers):
    """
    Procesa los clientes en orden de llegada y retorna el orden de atención.
    """
    queue = deque(customers)
    order_processed = []
    
    while queue:
        current_customer = queue.popleft()
        order_processed.append(current_customer)
    
    return order_processed

# Ejemplo de uso
if __name__ == "__main__":
    clients = ["Cliente1", "Cliente2", "Cliente3"]
    print(simulate_queue(clients))  # ["Cliente1", "Cliente2", "Cliente3"]

5.2 BFS (Búsqueda por Anchura)

Enunciado: Realizar un recorrido en anchura sobre un grafo, usando una cola.

Análisis
	•	Partimos de un nodo raíz/inicial.
	•	Mantenemos una cola donde encolamos el nodo de inicio.
	•	Mientras la cola no esté vacía, desencolamos un nodo y visitamos sus vecinos no visitados.
	•	Complejidad temporal: ￼, donde ￼ es el número de vértices y ￼ el número de aristas.
	•	Espacio adicional: ￼.

Implementación en Python

from collections import deque

def bfs(graph, start):
    """
    Realiza BFS en un grafo representado por un diccionario: nodo -> lista de vecinos
    """
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order

# Ejemplo de uso
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']

6. Problemas comunes sobre Tree

6.1 Recorridos: In-order, Pre-order, Post-order

Enunciado: Dado un árbol binario, se pide un método de recorrido para:
	1.	In-order (Izquierda - Raíz - Derecha)
	2.	Pre-order (Raíz - Izquierda - Derecha)
	3.	Post-order (Izquierda - Derecha - Raíz)

Análisis
	•	Se implementa de forma recursiva (o iterativa con pilas).
	•	Cada recorrido ofrece un orden distinto de visita.
	•	Complejidad temporal: ￼.

Implementación en Python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

# Ejemplo de uso
if __name__ == "__main__":
    # Construir un árbol simple: 
    #       1
    #      / \
    #     2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("In-order:", inorder_traversal(root))    # [2, 1, 3]
    print("Pre-order:", preorder_traversal(root))  # [1, 2, 3]
    print("Post-order:", postorder_traversal(root))# [2, 3, 1]

6.2 Altura del Árbol (Depth)

Enunciado: Calcular la altura (profundidad máxima) de un árbol binario, donde la altura se define como la longitud del camino más largo desde la raíz hasta una hoja.

Análisis
	•	Se implementa recursivamente.
	•	Altura de un árbol vacío es 0.
	•	Para cada nodo, la altura es 1 + max(altura(izq), altura(der)).
	•	Complejidad temporal: ￼.

Implementación en Python

def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

# Ejemplo de uso
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("Altura del árbol:", tree_height(root))  # 3

7. Problemas comunes con Grafos

7.1 BFS y DFS
	•	BFS: Ya mencionado en el apartado de colas.
	•	DFS (Depth-First Search): Podemos implementarlo de manera recursiva o iterativa (con una pila).

Implementación DFS Recursiva en Python

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

# Ejemplo de uso
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = dfs_recursive(graph, 'A')
    print(result)  # {'A', 'B', 'C', 'D', 'E', 'F'}

7.2 Dijkstra: Ruta Más Corta en Grafos con Pesos Positivos

Enunciado: Encontrar la distancia más corta desde un nodo origen hasta todos los demás en un grafo con pesos positivos.

Análisis
	1.	Iniciamos con la distancia al origen como 0 y a los demás nodos como infinito.
	2.	Utilizamos una cola de prioridad (heapq) para seleccionar en cada paso el nodo con la menor distancia acumulada.
	3.	“Relajamos” los vecinos del nodo actual: si encontramos un camino más corto, actualizamos la distancia.

	•	Complejidad temporal: ￼.
	•	Espacio adicional: ￼ para distancias.

Implementación en Python

import heapq

def dijkstra(graph, start):
    """
    El grafo está representado por un diccionario:
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('C', 1), ('D', 7)],
        ...
    }
    Retorna un diccionario con la distancia mínima desde 'start' a cada nodo.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]  # (distancia, nodo)
    
    while priority_queue:
        current_dist, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Ejemplo de uso
if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('C', 1), ('D', 7)],
        'C': [('A', 4), ('B', 1), ('D', 3)],
        'D': [('B', 7), ('C', 3)]
    }
    print(dijkstra(graph, 'A'))
    # Por ejemplo: {'A': 0, 'B': 2, 'C': 3, 'D': 6}

7.3 Detección de Ciclos

Enunciado: Verificar si un grafo contiene un ciclo. El método difiere si el grafo es dirigido o no dirigido.

Análisis (Grafo Dirigido)
	•	Se usa DFS con un conjunto de nodos en la “pila de recursión”.
	•	Si durante la exploración llegamos a un nodo que ya está en la pila de recursión, hay un ciclo.

Implementación en Python

def detect_cycle_dfs(graph):
    """
    Retorna True si el grafo dirigido 'graph' tiene un ciclo, False en caso contrario.
    graph = {
      'A': ['B'],
      'B': ['C'],
      ...
    }
    """
    visited = set()
    recursion_stack = set()
    
    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True
        
        recursion_stack.remove(node)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    graph_no_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    graph_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    print(detect_cycle_dfs(graph_no_cycle))  # False
    print(detect_cycle_dfs(graph_cycle))     # True

Conclusiones y Buenas Prácticas
	1.	Escoger la Estructura de Datos Correcta:
	•	Usar diccionarios (hash maps) para búsquedas rápidas.
	•	Stacks para problemas de tipo LIFO (balanceo de paréntesis, notación postfija).
	•	Queues (FIFO) para BFS o sistemas de espera.
	•	Árboles y grafos para relaciones jerárquicas o conexiones entre nodos.
	2.	Analizar la Complejidad:
	•	Determinar cuándo pasamos de una solución ￼ a una de ￼ es clave en problemas con grandes entradas.
	•	Notar la diferencia entre espacio adicional y espacio total.
	3.	Modularidad y Legibilidad:
	•	Escribe funciones pequeñas y con responsabilidades claras.
	•	Usa nombres de variables descriptivas y docstrings.
	4.	Tests y Casos Borde:
	•	Verifica la solución con entradas pequeñas o vacías.
	•	Considera valores extremos o atípicos (enteros negativos, árboles con un solo nodo, grafos desconectados, etc.).
	5.	Uso de Librerías de Python:
	•	collections (p. ej. deque, Counter)
	•	heapq para colas de prioridad
	•	Estas librerías mejoran la eficiencia y la legibilidad del código.

Con estas soluciones, Aki, tienes una visión amplia de la resolución de problemas clásicos en coding interviews, reforzando tanto la lógica del algoritmo como las mejores prácticas de programación en Python. ¡Mucho éxito en tus próximas pruebas de código!