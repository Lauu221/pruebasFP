


import os
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, Dict, List, Tuple, TypeVar, Generic
from datetime import datetime
from src.entrega3.red_social.grafo import Grafo 
from src.entrega3.red_social.recorridos import Recorrido

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas


# Definición de clases Usuario y Relacion
class Usuario:
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: str):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

    @classmethod
    def parse(cls, cadena: str) -> 'Usuario':
        dni, nombre, apellidos, fecha_nacimiento = cadena.split(',')
        return cls(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellidos}"


class Relacion:
    _xx_num = 0 

    def __init__(self, interacciones: int, dias_activa: int):
        Relacion._xx_num += 1
        self.id = Relacion._xx_num
        self.interacciones = interacciones
        self.dias_activa = dias_activa

    @classmethod
    def of(cls, interacciones: int, dias_activa: int) -> 'Relacion':
        return cls(interacciones, dias_activa)

    def __str__(self):
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones: {self.interacciones})"



class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, tipo_grafo='no dirigido'):
        super().__init__(dirigido=(tipo_grafo == 'dirigido'))
        self.usuarios_dni = {}

    @classmethod
    def parse(cls, archivo_usuarios: str, archivo_relaciones: str) -> 'Red_social':
        red_social = cls()
        
        
        with open(archivo_usuarios, 'r') as f_usuarios:
            for linea in f_usuarios:
                usuario = Usuario.parse(linea.strip())
                red_social.add_vertex(usuario.dni)
                red_social.usuarios_dni[usuario.dni] = usuario

        
        with open(archivo_relaciones, 'r') as f_relaciones:
            for linea in f_relaciones:
                id_usuario1, id_usuario2, interacciones, dias_activa = linea.strip().split(',')
                interacciones, dias_activa = int(interacciones), int(dias_activa)
                usuario1 = red_social.usuarios_dni.get(id_usuario1)
                usuario2 = red_social.usuarios_dni.get(id_usuario2)
                
                if usuario1 and usuario2:
                    relacion = Relacion.of(interacciones, dias_activa)
                    red_social.add_edge(usuario1.dni, usuario2.dni)
                    
        return red_social

    def __str__(self):
        return f"Red social con {len(self.usuarios_dni)} usuarios"

if __name__ == "__main__":
    
    raiz = os.path.dirname(__file__)
    f1 = os.path.join(raiz, '..', 'relaciones_y_usuarios', 'usuarios.txt')
    f2 = os.path.join(raiz, '..', 'relaciones_y_usuarios', 'relaciones.txt')

    rrss = Red_social.parse(f1, f2)

    origen_dni = '251439091'
    destino_dni = '87345530M'

    origen = rrss.usuarios_dni.get(origen_dni)
    destino = rrss.usuarios_dni.get(destino_dni)

    G = rrss.to_networkx_graph()

    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color="pink", node_size=1500, font_size=10, font_weight="bold")
    plt.title("Red Social de Usuarios")
    plt.show()
