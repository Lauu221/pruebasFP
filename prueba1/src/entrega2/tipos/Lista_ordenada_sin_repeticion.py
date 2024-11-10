
'''LISTA ORDENADA SIN REPETICIONES'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Callable
from src.entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar("E")
R = TypeVar("R")

class Lista_ordenada_sin_repeticion(AgregadoLineal[E], Generic[E,R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order 
        self._added_order = []
    
    @classmethod
    
    def of(cls, order: Callable[[E], R]) -> Lista_ordenada_sin_repeticion[E, R]:
        return cls(order)
    
    def __index_order(self, e: E)-> int:
        for i, existing_element in enumerate(self._elements):
            if self._order(e) < self._order(existing_element):
                return i 
        return len(self._elements)
    
    def add(self, e: E) -> None:
        self._added_order.append(e)
        if e in self._elements:
            print(f'el elemento {e} ya exixte en la lista, se elimina con remove()')
            return
        index = self.__index_order(e)
        self._elements.insert(index, e)
        print(f'se añade {e}')
        

    def added_order(self) -> List[E]:
        return self._added_order
    
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        print(f"Elementos eliminados utilizando remove_all: {removed_elements}")
        return removed_elements 
      
    def elements(self)-> List[E]:
        return self._elements
    
    