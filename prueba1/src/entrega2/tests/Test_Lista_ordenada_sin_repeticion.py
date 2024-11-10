

from src.entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

lista = Lista_ordenada_sin_repeticion(lambda x: x)

lista.add(3)
lista.add(1)
lista.add(2)
lista.add(2)


print('___________')
print("los elementos se han añadido de tal forma:", lista.added_order())
print('lista ordenada sin repetidos:', lista.elements())