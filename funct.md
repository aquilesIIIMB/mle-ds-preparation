🔥 Lista de Funciones Útiles de Python para Arrays, Strings, Hash Tables, Stacks, Queues, Trees y Graphs 🔥

A continuación, te detallo las funciones y métodos más útiles para cada tipo de dato o estructura en Python, con ejemplos prácticos que puedes usar para superar tests de código en LeetCode, HackerRank, Codeforces y otros.

🚀 1. Arrays (Listas en Python)

Función/Método	Descripción	Ejemplo
len(arr)	Devuelve el número de elementos.	len([1, 2, 3])  # 3
arr.append(x)	Añade un elemento al final.	arr = [1, 2] → arr.append(3) → [1, 2, 3]
arr.pop()	Elimina y devuelve el último elemento.	arr = [1, 2, 3] → arr.pop() → [1, 2]
arr.insert(i, x)	Inserta x en la posición i.	arr.insert(1, 10) → [1, 10, 2, 3]
arr.remove(x)	Elimina la primera ocurrencia de x.	arr.remove(2) → [1, 3, 4]
arr.sort()	Ordena el array en su lugar.	arr.sort() → [1, 2, 3]
sorted(arr)	Devuelve una nueva lista ordenada.	sorted([3, 1, 2]) → [1, 2, 3]
arr.index(x)	Devuelve el índice de la primera ocurrencia de x.	[1, 2, 3].index(2) → 1
arr.count(x)	Cuenta cuántas veces aparece x.	[1, 2, 2, 3].count(2) → 2
reversed(arr)	Devuelve un iterador en orden inverso.	list(reversed([1, 2, 3])) → [3, 2, 1]

🚀 2. Strings (Cadenas de texto)

Función/Método	Descripción	Ejemplo
len(s)	Devuelve la longitud de la cadena.	len("hello") → 5
s.find(sub)	Devuelve el índice de la primera ocurrencia de sub.	"hello".find("e") → 1
s.index(sub)	Similar a find, pero lanza excepción si no existe.	"hello".index("l") → 2
s.count(sub)	Cuenta cuántas veces aparece sub.	"hello".count("l") → 2
s.replace(old, new)	Reemplaza old por new.	"hello".replace("l", "x") → hexxo
s.split(delim)	Divide la cadena en una lista usando delim.	"1,2,3".split(",") → ['1', '2', '3']
s.strip()	Elimina espacios en blanco al inicio y final.	" hello ".strip() → "hello"
s.join(iterable)	Une elementos de un iterable con s como separador.	" ".join(['a', 'b', 'c']) → "a b c"
s[::-1]	Invertir una string.	"hello"[::-1] → "olleh"

🚀 3. Hash Tables (Diccionarios en Python)

Función/Método	Descripción	Ejemplo
len(dict)	Devuelve el número de claves en el diccionario.	len({'a': 1, 'b': 2}) → 2
dict.keys()	Devuelve las claves del diccionario.	{'a': 1, 'b': 2}.keys() → ['a', 'b']
dict.values()	Devuelve los valores del diccionario.	{'a': 1, 'b': 2}.values() → [1, 2]
dict.items()	Devuelve pares clave-valor.	{'a': 1}.items() → [('a', 1)]
dict.get(key, default)	Devuelve el valor asociado a key, o default.	{'a': 1}.get('b', 0) → 0
dict.pop(key)	Elimina y devuelve el valor de key.	d = {'a': 1} → d.pop('a')
dict.update(other)	Actualiza el diccionario con otro.	d.update({'c': 3}) → {'a': 1, 'c': 3}

🚀 4. Stacks (Usando listas)

Función/Método	Descripción	Ejemplo
stack.append(x)	Empuja un elemento a la pila.	stack.append(1)
stack.pop()	Saca el elemento superior de la pila.	stack.pop()
stack[-1]	Devuelve el elemento superior sin eliminarlo.	stack[-1]

🚀 5. Queues (Usando collections.deque)

Función/Método	Descripción	Ejemplo
queue.append(x)	Encola un elemento al final.	queue.append(1)
queue.popleft()	Desencola el primer elemento.	queue.popleft()
queue[0]	Devuelve el primer elemento sin eliminarlo.	queue[0]

🚀 6. Trees (Árboles personalizados)

Función/Método	Descripción	Ejemplo
TreeNode.left	Referencia al hijo izquierdo del nodo.	node.left
TreeNode.right	Referencia al hijo derecho del nodo.	node.right
inorder_traversal()	Recorrido en orden (izquierda, nodo, derecha).	Ver ejemplo abajo.

🚀 7. Graphs (Usando listas y diccionarios)

Función/Método	Descripción	Ejemplo
graph[node]	Devuelve los vecinos de un nodo.	graph["A"]
len(graph)	Devuelve el número de nodos en el grafo.	len(graph)
BFS/DFS	Recorridos básicos.	Ver ejemplo abajo.

🔥 Ejemplos Prácticos de Uso

1. Recorrido in-order en un árbol binario

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Construcción de ejemplo
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
inorder_traversal(root)  # Output: 1 2 3

2. BFS en un grafo

def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

bfs(graph, "A")  # Output: A B C D E F

🔑 Conclusión

Estas funciones son esenciales en entrevistas técnicas, especialmente en problemas donde optimizar el tiempo es crucial. Algunas recomendaciones de práctica:
	•	Arrays: Two Sum, Maximum Subarray
	•	Strings: Longest Palindromic Substring
	•	Hash Tables: Group Anagrams, Subarray Sum Equals K
	•	Trees: Balanced Binary Tree, Lowest Common Ancestor
	•	Graphs: Number of Connected Components

¡Practica estos problemas en LeetCode o HackerRank y avísame si necesitas ayuda con alguno en particular! 😊