

from src.entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

lista = Lista_ordenada_sin_repeticion(lambda x: x)

lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)

# el enunciado nos dice: si el elemento añadido es el menor de todos los elementos de la lista, se posiciona el primero [0]
print('___________')
print("los elementos se han añadido de tal forma:", lista.added_order())
print('lista ordenada sin repetidos:', lista.elements())


print("______")

removed_element = lista.remove()
print("El elemento eliminado al utilizar remove():", removed_element)

lista.add(removed_element)

removed_elements = lista.remove_all()
