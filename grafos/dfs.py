from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    Encuentra el camino más corto en un grafo no ponderado usando BFS.
    
    Args:
        graph: Diccionario de adyacencia donde las claves son nodos y los valores son 
               listas de vecinos.
        start: Nodo inicial.
        end: Nodo final.
        
    Returns:
        El camino más corto como una lista de nodos, o lista vacía si no hay camino.
    """
    # Si el inicio y fin son iguales
    if start == end:
        return [start]
        
    # Cola para BFS
    queue = deque([(start, [start])])
    
    # Conjunto para nodos visitados
    visited = set([start])
    
    while queue:
        node, path = queue.popleft()
        
        # Explorar todos los vecinos
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [neighbor]  # Camino encontrado
                    
                # Marcar como visitado y agregar a la cola
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []  # No se encontró camino