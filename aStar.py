from queue import PriorityQueue
class Nodo:
    def __init__(self, estado, padre, costo=0, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo
        self.heuristica = heuristica
        
    def __lt__(self, otro):
        return (self.costo + self.heuristica) < (otro.costo + otro.heuristica)
def busqueda_a_estrella(estado_inicial, estado_final, funcion_sucesores, funcion_heuristica):
    nodo_inicial = Nodo(estado_inicial, None, 0, funcion_heuristica(estado_inicial, estado_final))
    frontera = PriorityQueue()
    frontera.put(nodo_inicial)
    explorados = set()
    
    while not frontera.empty():
        nodo_actual = frontera.get()
        estado_actual = nodo_actual.estado
        
        if estado_actual == estado_final:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            return camino[::-1]
        
        explorados.add(estado_actual)
        
        for estado_sucesor, costo_accion in funcion_sucesores(estado_actual):
            if estado_sucesor not in explorados:
                costo_sucesor = nodo_actual.costo + costo_accion
                heuristica_sucesor = funcion_heuristica(estado_sucesor, estado_final)
                nodo_sucesor = Nodo(estado_sucesor, nodo_actual, costo_sucesor, heuristica_sucesor)
                frontera.put(nodo_sucesor)
    
    return None

def funcion_sucesores(estado):
    # Retorna una lista de tuplas (sucesor, costo) para un estado dado
    sucesores = []
    if estado == 'A':
        sucesores.append(('B', 1))
        sucesores.append(('C', 3))
    elif estado == 'B':
        sucesores.append(('D', 5))
        sucesores.append(('E', 2))
    elif estado == 'C':
        sucesores.append(('E', 4))
        sucesores.append(('F', 6))
    elif estado == 'D':
        sucesores.append(('G', 3))
    elif estado == 'E':
        sucesores.append(('G', 6))
    elif estado == 'F':
        sucesores.append(('G', 7))
    return sucesores

def funcion_heuristica(estado, estado_final):
    # Retorna el valor heurístico de un estado dado
    valores_heuristicos = {'A': 6, 'B': 4, 'C': 2, 'D': 4, 'E': 2, 'F': 0, 'G': 0}
    return valores_heuristicos[estado]

camino = busqueda_a_estrella('A', 'G', funcion_sucesores, funcion_heuristica)
print(camino) # Output: ['A', 'B', 'E', 'G']
