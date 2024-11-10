

''' COLA PRIORIDAD '''

from __future__ import annotations
from typing import TypeVar, Generic, Tuple, List, Callable
from src.entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar("E")
P = TypeVar("P")


class ColaPrioridad(Generic[E, P]):
    def __init__(self, order: Callable[[P], P] = lambda p: p):
       
        self._elements: List[E] = []  
        self._priorities: List[P] = [] 
        self._order = order  
    
    def size(self) -> int:
      
        return len(self._elements)

    def is_empty(self) -> bool:
        
        return len(self._elements) == 0  

    def elements(self) -> List[E]:
       
        return self._elements
    
    def add(self, e: E, priority: P) -> None:
       
        index = self.__index_order(priority)  
        self._elements.insert(index, e)  
        self._priorities.insert(index, priority)  
    
    def __index_order(self, priority: P) -> int:
        
        for i, existing_priority in enumerate(self._priorities):
            if self._order(priority) < self._order(existing_priority):
                return i
        return len(self._elements)
    
    def remove(self) -> E:
       
        assert len(self._elements) > 0, 'El agregado está vacío' 
        removed_element = self._elements.pop(0) 
        self._priorities.pop(0)  
        return removed_element
    
    def remove_all(self) -> List[E]:
        
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())  
        return removed_elements
    
    def __repr__(self) -> str:

        return f"ColaPrioridad({list(zip(self._elements, self._priorities))})"