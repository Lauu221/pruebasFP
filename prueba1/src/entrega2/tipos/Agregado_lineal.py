
''' AGREGADO LINEAL'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

E = TypeVar("E") 
# definimos un tipo genérico para los elementos, E puede recibir y devolver cualquier tipo 

class AgregadoLineal(ABC, Generic[E]):
    
    _elements: List[E] #creamos una lista de elementos tipo genérico E 

# iniciamos la lista, la cual está vacía  
    def __init__(self):
        self._elements = []
        
    @property
    def size(self)-> int:
        return len(self._elements) #nos dice cuantos elementos hay 
    
    def is_empty(self)-> bool:
        return len(self._elements) == 0 # true si no tiene elementos, false en caso contrario
    
    def elements(self)-> list[E]:
        return self._elements.copy() # devuelve copia de la lista interna 
    
    @abstractmethod
    
    def add(self, e:E)-> None: # metodo abstracto para añadir un elemento 
        pass 
    
    def add_all(self, ls:list[E])-> None:
        for element in ls:
            self.add(element) # agregar todos los elementos de ls a la lista interna
            
    def remove(self)-> E: # elimina y devuelve el primer elemento agregado a una lista interna
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)
    
    def remove_all(self)-> list[E]: #elimina los elementos de una lista y devuelve una nueva lista con los elementos eliminados 
        remove_elements = [] #nueva lista 
        while not self.is_empty:
            remove_elements.append(self.remove())
        return remove_elements
    
class Pila(AgregadoLineal[E]): # subclase LIFO, el ultimo elemento que agreguemos será el primero en sacarlo
    
    
    def add(self, e:E)->None:
        self._elements.append(e)
        
    def remove(self)-> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop()

class Cola(AgregadoLineal[E]): # subclase FIFO, el primer elemento que agreguemos, será el primero en sacarlo
    def add(self, e:E) ->None:
        self._elements.append(e)
        
    def remove(self)-> E:
        assert len(self.elements) >0, 'El agregado está vacío'
        return self._elements.pop(0)

            
    
    