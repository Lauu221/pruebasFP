
from src.entrega2.tipos.Cola import cola

cola = cola.of()

cola.add_all([23, 47, 1, 2, -3, 4, 5])
print('resultado de la cola:', cola)

print('________')
print(f'elementos eliminados utilizando remove_all: {cola}')