

'''EXAMEN 2'''

'''Ejercicio 1'''


from typing import List, TypeVar, Generic, Callable

E = TypeVar('E')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self.elementos: List[E] = []  

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        return iter(self.elementos)


    def contains(self, e: E) -> bool:
        return e in self.elementos
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for elemento in self.elementos:
            if func(elemento):
                return elemento
        return None
    
    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [elemento for elemento in self.elementos if func(elemento)]





class ColaConLimite(Agregado_lineal):
    def __init__(self, capacidad):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        self.capacidad = capacidad

    def add(self, elemento):
       
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self.elementos.append(elemento)
    
    def remove(self):
        if not self.elementos:
            raise IndexError("La cola está vacía.")
        return self.elementos.pop(0)

    def is_full(self):
        return len(self.elementos) >= self.capacidad

    @classmethod
    def of(cls, capacidad):
        return cls(capacidad)

print("test ejercicio 1:")
try:
    cola = ColaConLimite.of(3)
    cola.add(1)
    cola.add(2)
    cola.add(3)
    print("Estado actual de la cola:", list(cola))
    cola.add(4)  
except OverflowError as e:
    print("Error:", e)

print('____________________')

print('Ejercicio 2:')

def pruebas_agregado_lineal():
    print("=== Pruebas de Agregado_lineal ===")

    agregado = Agregado_lineal()
    agregado.elementos = [1, 2, 3, 4, 5]

    
    print("Prueba contains:")
    print("Contiene 3:", agregado.contains(3))  
    print("Contiene 10:", agregado.contains(10))  

    
    print("\nPrueba find:")
    print("Primer elemento > 2:", agregado.find(lambda x: x > 2))  # 3
    print("Primer elemento > 10:", agregado.find(lambda x: x > 10))  # None

    
    print("\nPrueba filter:")
    print("Elementos pares:", agregado.filter(lambda x: x % 2 == 0))  # [2, 4]
    print("Elementos > 3:", agregado.filter(lambda x: x > 3))  # [4, 5]


def pruebas_cola_con_limite():
    print("\n=== Pruebas de ColaConLimite ===")

    
    print("Prueba add e is_full:")
    cola = ColaConLimite.of(3)
    cola.add("a")
    cola.add("b")
    cola.add("c")
    print("La cola está llena:", cola.is_full())  
    try:
        cola.add("d")  
    except OverflowError as e:
        print("Error esperado al agregar en una cola llena:", e)

    
    print("\nPrueba remove:")
    print("Elemento eliminado:", cola.remove())  
    print("Elemento eliminado:", cola.remove())  
    print("Elemento eliminado:", cola.remove())  
    try:
        cola.remove()  
    except IndexError as e:
        print("Error esperado al eliminar de una cola vacía:", e)

    
    print("\nPrueba contains en ColaConLimite:")
    cola.add("task1")
    cola.add("task2")
    print("La cola contiene 'task1':", cola.contains("task1"))  
    print("La cola contiene 'task3':", cola.contains("task3"))  

    
    print("\nPrueba find en ColaConLimite:")
    print("Primer elemento que contiene '2':", cola.find(lambda x: "2" in x))  
    print("Primer elemento que contiene '3':", cola.find(lambda x: "3" in x))  

    
    print("\nPrueba filter en ColaConLimite:")
    cola.add("task3")
    print("Elementos que contienen 'task':", cola.filter(lambda x: "task" in x))  
    print("Elementos que terminan en '3':", cola.filter(lambda x: x.endswith("3")))  

    
    print("\nPruebas de casos límite:")
    cola_vacia = ColaConLimite.of(1)
    print("La cola vacía está llena:", cola_vacia.is_full())  
    try:
        print("Intentar eliminar de una cola vacía:")
        cola_vacia.remove()  
    except IndexError as e:
        print("Error esperado al eliminar de una cola vacía:", e)



if __name__ == "__main__":
    pruebas_agregado_lineal()
    pruebas_cola_con_limite()