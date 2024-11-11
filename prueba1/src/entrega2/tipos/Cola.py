

'''COLA'''
from __future__ import annotations
from typing import TypeVar, Generic, List
from src.entrega2.tipos.Agregado_lineal import AgregadoLineal


E = TypeVar("E")

class cola(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()
        print('creamos una cola vacía')
        
    @classmethod
    def of(cls)-> cola[E]:
        return cls()
    
    def add(self, e: E)-> None:
        self._elements.append(e)
       
    
    def add_all(self, elements: List[E]) -> None:
        for e in elements:
            self.add(e)
        
        print(f"se añaden con un solo metodo los números: {', '.join(map(str, elements))}")
        
        
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        print(f"Elementos eliminados utilizando remove_all: {removed_elements}")
        return removed_elements 
      


    def elements(self) -> List[E]:
        return self._elements
    
    def __repr__(self)-> str:
        return f'cola({self._elements})'