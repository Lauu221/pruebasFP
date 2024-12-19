
'''ejercicio 1'''
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(archivo: str):
      
        '''Método para leer un fichero genes.txt y procesar cada línea para crear objetos Gen.'''
        genes = []
        try:
            with open(archivo, "r") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) != 4:
                        print(f"Error: La línea no tiene el formato esperado: {linea.strip()}")
                        continue
                    
                    nombre = partes[0].strip()
                    tipo = partes[1].strip()
                    try:
                        num_mutaciones = int(partes[2].strip())
                    except ValueError:
                        print(f"Error: El número de mutaciones debe ser un entero válido en la línea: {linea.strip()}")
                        continue
                    
                    loc_cromosoma = partes[3].strip()
                    try:
                        gen = Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)
                        genes.append(gen)
                    except ValueError as e:
                        print(f"Error: {e} en la línea: {linea.strip()}")
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no se encontró.")
        return genes


'''ejercicio 2'''

from dataclasses import dataclass


@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not (-1 <= conexion <= 1):
            raise ValueError("El valor de conexión debe estar entre -1 y 1 (ambos inclusive).")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(archivo: str):
        relaciones = []
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                for linea in file:
                    if linea.strip():  
                        try:
                            relaciones.append(RelacionGenAGen.parse(linea.strip()))
                        except ValueError as e:
                            print(f"Error al procesar la línea '{linea.strip()}': {e}")
        except FileNotFoundError:
            raise ValueError(f"No se encontró el archivo: {archivo}")
        return relaciones

    @staticmethod
    def parse2(linea: str):
        partes = linea.strip().split(",")
        if len(partes) != 3:
            raise ValueError("La línea no tiene el formato esperado: nombre_gen1,nombre_gen2,conexion")
        
        nombre_gen1 = partes[0].strip()
        nombre_gen2 = partes[1].strip()
        try:
            conexion = float(partes[2].strip())
        except ValueError:
            raise ValueError("El valor de conexión debe ser un número real.")
        
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

    
''' ejercicio 3'''
   
   

from dataclasses import dataclass, field
from typing import Dict, TypeVar, Generic, Callable, Optional, Set, List
from datetime import date
import os
import matplotlib.pyplot as plt
import networkx as nx


V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas




class Grafo(Generic[V, E]):
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}

    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
        return Grafo(es_dirigido)
    
    def add_vertex(self, vertice: V) -> bool:
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
            return True
        return False

    def add_edge(self, origen: V, destino: V, arista: E) -> bool:
        if origen not in self.adyacencias: 
            self.add_vertex(origen)
        if destino not in self.adyacencias: 
            self.add_vertex(destino)
        
        if origen == destino:  # no permitir bucles
            return False
        if not self.es_dirigido:
            if destino in self.adyacencias[origen] or origen in self.adyacencias[destino]:
                return False
            self.adyacencias[origen][destino] = arista  # arista en ambas direcciones 
            self.adyacencias[destino][origen] = arista
        else:
            if destino in self.adyacencias[origen]:
                return False
            self.adyacencias[origen][destino] = arista
        return True
    
    def dfs(self,grafo: Grafo[V, E], inicio: V, objetivo: V, visitados: Optional[Set[V]] = None, camino: Optional[List[V]] = None) -> List[V]: 
        if visitados is None: 
            visitados = set() 
        if camino is None: 
            camino = [] 
        visitados.add(inicio) 
        camino.append(inicio) 
        
        if inicio == objetivo: 
                return camino 
        for vecino in grafo.successors(inicio): 
            if vecino not in visitados: 
                resultado = dfs(grafo, vecino, objetivo, visitados, camino) 
                if resultado: 
                        return resultado
                    
        camino.pop() 
        return []
    def successors(self, vertice: V) -> set[V]:
        if vertice not in self.adyacencias: 
            raise ValueError(f'el vertice {vertice} no existe en el grafo')
        return set(self.adyacencias[vertice].keys())

    def predecessors(self, vertice: V) -> set[V]:
        if not self.es_dirigido:
            return self.successors(vertice)
        return {origen for origen, destinos in self.adyacencias.items() if vertice in destinos}

    def edge_weight(self, origen: V, destino: V) -> Optional[E]:
        if origen in self.adyacencias and destino in self.adyacencias[origen]:
            return self.adyacencias[origen][destino]
        return None

    def vertices(self) -> set[V]:
        return set(self.adyacencias.keys())

    def edge_exists(self, origen: V, destino: V) -> bool:
        return destino in self.adyacencias.get(origen, {})

    def subgraph(self, vertices: set[V]) -> Grafo[V, E]:
        subgrafo = Grafo(self.es_dirigido)
        for vertice in vertices:
            if vertice in self.adyacencias:
                subgrafo.add_vertex(vertice)
                for destino, arista in self.adyacencias[vertice].items():
                    if destino in vertices:
                        subgrafo.add_edge(vertice, destino, arista)
        return subgrafo

    def inverse_graph(self) -> Grafo[V, E]:
        if not self.es_dirigido:
            raise ValueError("El grafo no es dirigido, no se puede invertir.")
        
        nuevo_grafo = Grafo[V, E](es_dirigido=True)
        
        for origen in self.adyacencias:
            for destino, arista in self.adyacencias[origen].items():
                nuevo_grafo.add_edge(destino, origen, arista)
        return nuevo_grafo

    def draw(self, titulo: str = "Grafo", lambda_vertice: Callable[[V], str] = str, lambda_arista: Callable[[E], str] = str) -> None:
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
        for vertice in self.adyacencias:
            G.add_node(lambda_vertice(vertice))
        for origen in self.adyacencias:
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(lambda_vertice(origen), lambda_vertice(destino), label=lambda_arista(arista))
        
        plt.figure(figsize=(10, 8))
        nx.draw(G, with_labels=True, node_color="pink", node_size=1500, font_size=10, font_weight="bold")
        plt.title(titulo)
        plt.show()
    
    def __str__(self):
        representacion = [] 
        for vertice in self.vertices(): 
            relaciones = [] 
            for vecino in self.adyacencias[vertice]: 
                relacion = f"{vertice} -> {vecino} ({self.adyacencias[vertice][vecino]})" 
                relaciones.append(relacion) 
                representacion.extend(relaciones) 
                return "\n".join(representacion)
    


if __name__ == "__main__":
    try:
        archivo_genes = "genes.txt"  
        genes = Gen.parse(archivo_genes)
        print("tipos de genes :")
        for gen in genes:
            print(gen)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        archivo_red_genes = "red_genes.txt"
        genes = RelacionGenAGen.parse(archivo_red_genes)
        print("relaciones :")
        for gen in genes:
            print(gen)
    except ValueError as e:
        print(f"Error: {e}")
    try: 
        genes_txt = 'genes.txt' 
        red_genes_txt = 'red_genes.txt' 
        grafo_genico = Grafo.of(es_dirigido=False) 
        
        gen_inicio = 'TP53' 
        gen_objetivo = 'APC' 
        camino = Grafo.dfs(grafo_genico, gen_inicio, gen_objetivo)
        subgrafo = grafo_genico.subgraph(set(camino)) 
        subgrafo.draw(titulo="Subgrafo desde KRAS hasta PIK3CA", lambda_vertice=str, lambda_arista=str)
    except ValueError as e:
        print(f"Error: {e}")    