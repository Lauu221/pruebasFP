'''
Created on 21 nov 2024

@author: damat
'''
from __future__ import annotations

from typing import TypeVar, Generic, Dict, Set, Optional, Callable, List, Tuple
import matplotlib.pyplot as plt
import networkx as nx

# Definición de tipos genéricos
V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

class Grafo(Generic[V, E]):
    """
    Representaciónde un grafo utilizando un diccionario de adyacencia.
    """
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}  # Diccionario de adyacencia
        
    
    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
        return Grafo(es_dirigido)
        """
        Método de factoría para crear un nuevo grafo.
        
        :param es_dirigido: Indica si el grafo es dirigido (True) o no dirigido (False).
        :return: Nuevo grafo.
        """
        
    
    def add_vertex(self, vertice: V) -> None:
        
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
            return True
        return False
       
            
        """
        Añade un vértice al grafo si no existe.
        
        :param vertice: Vértice a añadir.
        """
        

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        
        
        if origen not in self.adyacencias: 
            self.add_vertex(origen)
        if destino not in self.adyacencias: 
            self.add_vertex(destino)
        
        if origen == destino: # no permitir bucles
            return False
        if not self.es_dirigido:
            if destino in self.adyacencias[origen] or origen in self.adyacencias[destino]:
                return False
            self.adyacencias[origen][destino] = arista #arista en ambas direcciones 
            self.adyacencias[destino][origen] = arista
        else:
            if destino in self.adyacencias[origen]:
                return False
            self.adyacencias[origen][destino] = arista
        return True
        
    
        
        """
        Añade una arista al grafo entre dos vértices.
        Si el grafo es no dirigido, añade la arista en ambos sentidos.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :param arista: Arista a añadir.
        """
    
    def successors(self, vertice: V) -> Set[V]:
        
        if vertice not in self.adyacencias: 
            raise ValueError(f'el vertice {vertice} no existe en el grafo')
        return set(self.adyacencias[vertice].keys())
        """
        Devuelve los sucesores de un vértice.
        
        :param vertice: Vértice del que se buscan los sucesores.
        :return: Conjunto de sucesores.
        """
        

    def predecessors(self, vertice: V) -> Set[V]:
        
        if not self.es_dirigido:
            return self.successors(vertice)
        return {origen for origen, destinos in self.adyacencias.items() if vertice in destinos} 
        """
        Devuelve los predecesores de un vértice.
        
        :param vertice: Vértice del que se buscan los predecesores.
        :return: Conjunto de predecesores.
        """
   
    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        
        if origen in self.adyacencias and destino in self.adyacencias[origen]:
            return self.adyacencias[destino][origen]
        return None
        """
        Devuelve el peso de la arista entre dos vértices.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: Peso de la arista, o None si no existe.
        """
        

    def vertices(self) -> Set[V]:
        return set(self.adyacencias.keys())
        """
        Devuelve el conjunto de vértices del grafo.
        
        :return: Conjunto de vértices.
        """
        
    
    def edge_exists(self, origen: V, destino: V) -> bool:
        if origen in self.andyacencias and destino in self.adyacencias[origen]:
            return True
        """
        Verifica si existe una arista entre dos vértices.
        
        :param origen: Vértice de origen.
        :param destino: Vértice de destino.
        :return: True si existe la arista, False en caso contrario.
        """
       

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        subgrafo = Grafo(self.es_dirigido)
        for vertice in vertices:
            if vertice in self.adyacencias:
                subgrafo.add_vertex(vertice)
                for destino, arista in self.adyacencias[vertice].items():
                    if destino in vertices:
                        subgrafo.add_edge(vertice, destino, arista)
        return subgrafo
        """
        Crea un subgraph basado en un conjunto de vértices.
        
        :param vertices: Conjunto de vértices del subgraph.
        :return: Nuevo grafo con los vértices y aristas correspondientes.
        """
        

    def inverse_graph(self) -> Grafo[V, E]:
        
        if not self.es_dirigido:
            raise ValueError("El grafo no es dirigido, no se puede invertir.")
    
        nuevo_grafo = Grafo[V, E](es_dirigido=True)
    
        for origen in self.adyacencias:
            for destino, arista in self.adyacencias[origen].items():
                nuevo_grafo.add_edge(destino, origen, arista)
        return nuevo_grafo

        """
        Devuelve el grafo inverso (solo válido para grafos dirigidos).
        
        :return: Grafo inverso.
        :raise ValueError: Si el grafo no es dirigido.
        """
        

    def draw(self, titulo: str = "Grafo", 
            lambda_vertice: Callable[[V], str] = str, 
            lambda_arista: Callable[[E], str] = str) -> None:
        """
        Dibuja el grafo utilizando NetworkX y Matplotlib. las funciones lambda permiten personalizar la representación
        de los vértices y aristas.
        
        :param titulo: Título del gráfico
        :param lambda_vertice: Función lambda para representar los vértices
        :param lambda_arista: Función lambda para representar las aristas
        """
        # Crear un grafo de NetworkX
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        # Añadir nodos y aristas
        for vertice in self.vertices():
            G.add_node(vertice, label=lambda_vertice(vertice))  # Usamos lambda_vertice para personalizar el nodo
        for origen in self.vertices():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista))  # Usamos lambda_arista para personalizar la arista
    
        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Distribución de los nodos
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, 
                labels=nx.get_node_attributes(G, 'label'))  # Usamos las etiquetas personalizadas de los vértices
    
        # Dibujar las etiquetas de las aristas (con la representación personalizada)
        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
        plt.title(titulo)
        plt.show()

        
    def __str__(self) -> str:
        
        representacion = []
        
        for vertice in self.vertices:
            relaciones = []
            for vecino in self.adyacentes(vertice):
                relacion = f"{vertice.dni} -> {vecino.dni} ({vecino.tipo.id})"
                relaciones.append(relacion)
            representacion.extend(relaciones)
        
        return "\n".join(representacion)

        """
        Representación textual del grafo.
        
        Formato libre. Por ejemplo:
            vertice1 -> vertice2 (peso), vertice3 (peso)
            vertice2 -> vertice1 (peso)
            ...
        """
        

if __name__ == '__main__':
    # Crear un grafo dirigido
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    
    # Dibujar el grafo
    #grafo.draw(titulo="Mi Grafo Dirigido")
    
    grafo.inverse_graph().draw(titulo="Inverso del Grafo Dirigido")
