from __future__ import annotations
from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from src.entrega3.red_social.recorridos import bfs
from src.entrega3.red_social.grafo import Grafo
import os

raiz = os.path.dirname(__file__)
f1 = os.path.join(os.path.dirname(__file__), '..', 'relaciones_y_usuarios', 'usuarios.txt')
f2 = os.path.join(os.path.dirname(__file__), '..', 'relaciones_y_usuarios', 'relaciones.txt')


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    def __str__(self) -> str:
        return f"Usuario(dni={self.dni}, nombre={self.nombre}, apellidos={self.apellidos}, fecha_nacimiento={self.fecha_nacimiento})"
        

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 
    
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)
    
    def __str__(self) -> str:
        return f"Relacion(id={self.id}, interacciones={self.interacciones}, dias_activa={self.dias_activa})"
        

class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        return Red_social(es_dirigido)
    
    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> 'Red_social':
        red_social = Red_social(es_dirigido)
        try:
            with open(f1, "r", encoding="utf-8") as archivo_usuarios:
                for linea in archivo_usuarios:
                    dni, nombre, apellidos, fecha = linea.strip().split(",")
                    usuario = Usuario.of(dni, nombre, apellidos, date.fromisoformat(fecha))
                    if usuario.dni not in red_social.usuarios_dni:
                        red_social.usuarios_dni[dni] = usuario
                        red_social.add_vertex(usuario)
                        
        except FileNotFoundError:
            print(f"Archivo de usuarios no encontrado: {f1}")
            raise
        
        try:
            with open(f2, "r", encoding="utf-8") as archivo_relaciones:
                for linea in archivo_relaciones:
                    origen_dni, destino_dni, interacciones, dias_activa = linea.strip().split(",")
                    origen = red_social.usuarios_dni.get(origen_dni, Usuario.of(origen_dni, "Usuario Provisional", "Apellido Provisional", date(1900, 1, 1)))
                    destino = red_social.usuarios_dni.get(destino_dni, Usuario.of(destino_dni, "Usuario Provisional", "Apellido Provisional", date(1900, 1, 1)))
                    if origen and destino:
                        relacion = Relacion.of(int(interacciones), int(dias_activa))
                        red_social.add_edge(origen, destino, relacion)
                        
        except FileNotFoundError:
            print(f"Archivo de relaciones no encontrado: {f2}")
            raise

        return red_social


if __name__ == '__main__':
    f1 = os.path.join(os.path.dirname(__file__), '..', 'relaciones_y_usuarios', 'usuarios.txt')
    f2 = os.path.join(os.path.dirname(__file__), '..', 'relaciones_y_usuarios', 'relaciones.txt')
    
    rrss = Red_social.parse(f1, f2, es_dirigido=False)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    
    origen_dni = '25143909I' 
    destino_dni = '87345530M' 
    
    origen = rrss.usuarios_dni.get(origen_dni)
    destino = rrss.usuarios_dni.get(destino_dni)
    camino = bfs(rrss, origen, destino)
    
    g_camino = rrss.subgraph(camino)
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.nombre} {v.apellidos}", lambda_arista=lambda e: e.id)
