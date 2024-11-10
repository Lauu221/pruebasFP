


from src.entrega2.tipos.Lista_ordenada import Lista_ordenada




lista = Lista_ordenada(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)

print("Se añade en este orden:", lista.added_order())
print("Lista ordenada:", lista.elements())

