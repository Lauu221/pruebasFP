

from src.entrega2.tipos.Pila import Pila

# creamos un ejemplo simple 

pila = Pila.of()

pila.add(1)
pila.add(2)
pila.add(3)

print(pila.elements())

tope = pila.pop()
print(f'el tope de la lista es: {tope}')
print('eliminamos el primer elemento de la lista (el tope):')
print(pila.elements())

