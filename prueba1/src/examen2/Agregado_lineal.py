
''' AGREGADO LINEAL'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

E = TypeVar("E") 


class AgregadoLineal(ABC, Generic[E]):
    
    _elements: List[E] 


    def __init__(self):
        self._elements = []
        
    @property
    def size(self)-> int:
        return len(self._elements)  
    
    def is_empty(self)-> bool:
        return len(self._elements) == 0 
    
    def elements(self)-> list[E]:
        return self._elements.copy()  
    
    @abstractmethod
    
    def add(self, e:E)-> None:  
        pass 
    
    def add_all(self, ls:list[E])-> None:
        for element in ls:
            self.add(element) 
            
    def remove(self)-> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)
    
    def remove_all(self)-> list[E]: 
        remove_elements = [] 
        while not self.is_empty:
            remove_elements.append(self.remove())
        return remove_elements
    
class Pila(AgregadoLineal[E]): 
    
    
    def add(self, e:E)->None:
        self._elements.append(e)
        
    def remove(self)-> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop()

class Cola(AgregadoLineal[E]): 
    def add(self, e:E) ->None:
        self._elements.append(e)
        
    def remove(self)-> E:
        assert len(self.elements) >0, 'El agregado está vacío'
        return self._elements.pop(0)

            
    
    