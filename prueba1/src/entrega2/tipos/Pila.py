

from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod
from src.entrega2.tipos.Agregado_lineal import AgregadoLineal
from test.test_pydoc.pydocfodder import A_staticmethod

E = TypeVar("E")

class Pila(AgregadoLineal[E]):
    
    @staticmethod
    
    def of()-> 'Pila[E]':
        return Pila()
    def add(self, e: E)-> None:
        self._elements.insert(0, e)
    
    def pop(self)-> E:
        if self.is_empty():
            raise IndexError("La pila esta vacia")
        return self._elements.pop(0)
    

