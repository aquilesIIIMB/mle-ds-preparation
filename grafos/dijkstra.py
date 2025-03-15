import heapq

def dijkstra(graph, start, end):
    """
    Encuentra el camino más corto entre start y end usando el algoritmo de Dijkstra.
    
    Args:
        graph: Diccionario de adyacencia donde las claves son nodos y los valores son 
               listas de tuplas (vecino, peso).
        start: Nodo inicial.
        end: Nodo final.
        
    Returns:
        Una tupla con (distancia_total, camino) donde camino es una lista de nodos.
    """
    # Inicializar distancias como infinito para todos los nodos excepto el inicio
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Diccionario para reconstruir el camino
    previous = {node: None for node in graph}
    
    # Cola de prioridad para seleccionar el nodo con menor distancia
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si llegamos al nodo final, podemos terminar
        if current_node == end:
            break
            
        # Si ya encontramos un camino más corto a este nodo, lo ignoramos
        if current_distance > distances[current_node]:
            continue
            
        # Revisamos cada vecino del nodo actual
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Si encontramos un camino más corto al vecino, lo actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruir el camino
    if distances[end] == float('infinity'):
        return float('infinity'), []  # No hay camino
        
    path = []
    current = end
    
    while current:
        path.append(current)
        current = previous[current]
        
    # Invertir el camino ya que lo construimos desde el final
    path.reverse()
    
    return distances[end], path