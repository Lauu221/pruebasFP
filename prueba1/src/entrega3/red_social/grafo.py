from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    
    def __init__(self, dirigido=False):
        self.vertices = {}  # Diccionario de vértices
        self.aristas = {}  # Diccionario de aristas
        self.dirigido = dirigido

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = {'vecinos': set(), 'predecesores': set(), 'sucesores': set()}
            return True
        return False

    def add_edge(self, origen, destino):
        if origen == destino:  # No se permiten bucles
            return False
        if origen not in self.vertices or destino not in self.vertices:
            return False
        # Añadir la arista
        self.vertices[origen]['vecinos'].add(destino)
        self.vertices[destino]['vecinos'].add(origen)
        if self.dirigido:
            self.vertices[origen]['sucesores'].add(destino)
            self.vertices[destino]['predecesores'].add(origen)
        return True

    def to_networkx_graph(self):
        """Convierte el grafo en un grafo de networkx para su visualización"""
        G = nx.DiGraph() if self.dirigido else nx.Graph()
        for v in self.vertices:
            G.add_node(v)
        for origen in self.vertices:
            for destino in self.vertices[origen]['vecinos']:
                G.add_edge(origen, destino)
        return G


    def successors(self, vertice: V) -> Set[V]:
        if vertice not in self.vertices:
            raise ValueError(f'El vértice {vertice} no existe en el grafo')
        return self.vertices[vertice]['sucesores'] if self.dirigido else self.vertices[vertice]['vecinos']

    def predecessors(self, vertice: V) -> Set[V]:
        if not self.dirigido:
            return self.successors(vertice)
        if vertice not in self.vertices:
            raise ValueError(f'El vértice {vertice} no existe en el grafo')
        return self.vertices[vertice]['predecesores']

    def inverse_graph(self):
        if not self.dirigido:
            raise ValueError("El grafo no es dirigido, no se puede invertir.")
        nuevo_grafo = Grafo(dirigido=True)
        for vertice in self.vertices:
            nuevo_grafo.add_vertex(vertice)
        for origen in self.vertices:
            for destino in self.vertices[origen]['sucesores']:
                nuevo_grafo.add_edge(destino, origen)
        return nuevo_grafo

    def draw(self, titulo: str = "Grafo", 
             lambda_vertice: Callable[[V], str] = str, 
             lambda_arista: Callable[[E], str] = str) -> None:
        G = nx.DiGraph() if self.dirigido else nx.Graph()
        for vertice in self.vertices:
            G.add_node(vertice, label=lambda_vertice(vertice))
        for origen in self.vertices:
            for destino in self.vertices[origen]['vecinos']:
                G.add_edge(origen, destino)
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500)
        plt.title(titulo)
        plt.show()

    def __str__(self) -> str:
        representacion = []
        for vertice in self.vertices:
            relaciones = [f"{vertice} -> {vecino}" for vecino in self.vertices[vertice]['vecinos']]
            representacion.extend(relaciones)
        return "\n".join(representacion)


if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo(dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B")
    grafo.add_edge("B", "C")
    
   
    
    # Grafo inverso
    inverso = grafo.inverse_graph()
    inverso.draw(titulo="Inverso del Grafo Dirigido")