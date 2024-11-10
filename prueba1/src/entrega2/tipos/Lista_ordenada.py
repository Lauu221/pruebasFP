
'''LISTA ORDENADA'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Callable
from src.entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(AgregadoLineal[E]): # creamos la clase lista ordenada que maneja elementos de tipo generico (E)
    def __init__(self, order: Callable[[E], R]): # inicia la clase y se ejecuta cada vez que se crea un objeto
        super().__init__() # llama al constructor de la clase base para asegurarse de que se ejecute cualquier inicializacion necesaria
        self.order = order # permite que order este disponible en otros metodos 
        self._added_order = [] # almacena los elementos
        
    @classmethod   
    
    
    def of(cls, order: Callable[[E],R])-> Lista_ordenada[E,R]: # cls indica que of es un metodo de clase 
        return cls(order)
    
    def __index_order(self, e: E) -> int: # busca la posicion adecuada para insertar un elemento e en una lista (self._elements)
        for i, existing_element in enumerate(self._elements):
            if self.order(e) < self.order(existing_element):
                return i
        return len(self._elements)
    
    
    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)  
        self._added_order.append(e)  
        print(f"Se añade: {e}")
        

    def remove(self)-> E:
        assert len(self._elements) > 0, 'el agregado no existe'
        return self._elements.pop(0)
    
    def added_order(self) -> List[E]:
        return self._added_order
    
    def elements(self)-> List[E]:
        return self._elements
    

   