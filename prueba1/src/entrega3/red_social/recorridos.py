'''
Created on 21 nov 2024

@author: damat

-------------
Pseudocódigo:
-------------

función bfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una cola vacía
    agregar inicio a la cola
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la cola no esté vacía:
        tomar el elemento que está al frente de la cola y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo:
                si vecino no está en visitados:
                    agregar vecino a la cola
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)

-------------------------------------------------------------
función dfs(grafo, inicio, destino):
    crear un conjunto vacío llamado visitados
    crear una pila vacía
    agregar inicio a la pila
    crear un diccionario llamado predecesores, donde inicio no tiene predecesor

    mientras la pila no esté vacía:
        tomar el elemento más reciente agregado a la pila y llamarlo vértice

        si vértice es igual a destino:
            salir del bucle

        si vértice no está en visitados:
            agregar vértice al conjunto visitados

            para cada vecino conectado a vértice en el grafo, en orden inverso:
                si vecino no está en visitados:
                    agregar vecino a la pila
                    registrar a vértice como predecesor de vecino en predecesores

    devolver reconstruir_camino(predecesores, destino)
-------------------------------------------------------------------------

función reconstruir_camino(predecesores, destino):
    crear una lista vacía llamada camino
    establecer vértice_actual como destino

    mientras vértice_actual no sea nulo:
        agregar vértice_actual al inicio de la lista camino
        cambiar vértice_actual al predecesor de dicho vértice_actual usando el diccionario predecesores

    devolver camino

'''
from typing import TypeVar, List, Generic

from src.entrega3.red_social.grafo import Grafo


# Importa la clase Grafo desde su módulo

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

class Recorrido(Generic[V, E]):
    def __init__(self, grafo: Grafo[V, E], origen: V):
        self._grafo = grafo
        self._origen = origen
        self._tree = {}  # Estructura para almacenar el árbol de recorrido
        self._path = []  # Lista para almacenar el camino
        self._init_recorrido()

    def _init_recorrido(self):
        """Método para inicializar el recorrido, comenzando desde el origen"""
        # Iniciar el árbol con el origen
        self._tree[self._origen] = (None, 0.0)  # El origen no tiene predecesor y su distancia es 0
        self._path.append(self._origen)

    def bfs(self):
        """Método de recorrido en amplitud (BFS)"""
        visited = set()
        queue = [self._origen]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for neighbor in self._grafo.vertices[node]['vecinos']:
                    if neighbor not in visited:
                        self._tree[neighbor] = (node, self._tree[node][1] + 1)
                        queue.append(neighbor)
        return self._tree

    def dfs(self):
        """Método de recorrido en profundidad (DFS)"""
        visited = set()
        stack = [self._origen]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self._grafo.vertices[node]['vecinos']:
                    if neighbor not in visited:
                        self._tree[neighbor] = (node, self._tree[node][1] + 1)
                        stack.append(neighbor)
        return self._tree
    

def reconstruir_camino(predecesores: dict, destino: V) -> List[V]:
    
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = predecesores.get(actual, None)

    return camino[::-1]
    
    
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    
    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """
    
