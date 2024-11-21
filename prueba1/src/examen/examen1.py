

import string
from collections import Counter
from typing import List, Tuple
import os 
import math
file_path2 = os.path.join(os.path.dirname(__file__), '..', 'lecturas', 'archivo_palabras.txt')


''' ejercicio A '''

print('ejercicio A')

def P2(n: int, k: int) -> int:
    try:
        if n < 1 or k < 1:
            raise ValueError("n y k deben ser enteros positivos.")
        if n < k:
            raise ValueError("n debe ser mayor o igual que k.")
        producto = 1
        
        for i in range(1, k - 1 + 1):  
            producto *= (n - i + 1)
        
        return producto

    except ValueError as e:
        print(f"Error: {e}")
        return None  

# Ejemplo de uso
k = 3
n = 5
resultado = P2(n, k)
print(f"Resultado para P2({n}, {k}): {resultado}")

# Ejemplos adicionales
resultado_invalido = P2(2, 3)  # n < k, debería generar un error
print(f"Resultado para P2(2, 3): {resultado_invalido}")

resultado_negativo = P2(-5, 3)  # n negativo, debería generar un error
print(f"Resultado para P2(-5, 3): {resultado_negativo}")



print('................')


''' ejercicio B '''

print('ejercicio B')


def C2(n: int, k: int) -> int:
    try:

        if n < 1 or k < 1:
            raise ValueError("n y k deben ser enteros positivos.")
        if n < k:
            raise ValueError("n debe ser mayor o igual que k.")
        
        resultado = math.factorial(n) // (math.factorial(k + 1) * math.factorial(n - (k + 1)))
        return resultado

    except ValueError as e:
        print(f"Error: {e}")
        return None  
# Ejemplo 
resultado = C2(5, 3)
print(f' el resultado es {resultado}')

# Ejemplos adicionales
resultado_invalido = C2(2, 3)  # n < k, debería generar un error
print(f"Resultado para C2(2, 3): {resultado_invalido}")

resultado_negativo = C2(-5, 3)  # n negativo, debería generar un error
print(f"Resultado para C2(-5, 3): {resultado_negativo}")

print('................')


''' ejercicio C '''

print('ejercicio C')

def S2(n: int, k: int) -> float:
    try:

        if n < 1 or k < 1:
            raise ValueError("n y k deben ser enteros positivos.")  # Si n y k no son enteros positivos, lanza un ValueError
        
        if n < k:
            raise ValueError("n debe ser mayor o igual que k.")  # Si n es menor que k, lanza un ValueError
        
        division_externa = math.factorial(k) / (n * math.factorial(k + 2))
        
        sumatorio = 0  # Comienza en 0
        for i in range(k + 1):
            binomial = math.comb(k, i)
            signo = (-1) ** i
            potencia = (k - i) ** (n + 1)
            sumatorio += signo * binomial * potencia
        
        resultado = division_externa * sumatorio
        
        return resultado

    except ValueError as e:
        print(f"Error: {e}")
        return None  

# Ejemplo de uso
n = 5
k = 3
resultado = S2(n, k)
print(f'el resultado es {resultado}')

# Ejemplos adicionales
resultado_invalido = S2(2, 3)  # n < k, debería generar un error
print(resultado_invalido)

resultado_negativo = S2(-5, 3)  # n negativo, debería generar un error
print(resultado_negativo)


print('................')

''' ejercicio D '''

print('ejercicio D')

def palablasMasComunes(fichero: str, n: int)-> List[Tuple[str, int]]:
    assert n > 1, "n debe ser mayor que 1"
    try:
        with open(fichero, "r", encoding="utf-8") as file:
            contenido = file.read()
            contenido = contenido.lower() # pasa el contenido a minúsculas para no diferenciar 
            contenido = contenido.translate(str.maketrans("", "", string.punctuation)) # elimina los signos de puntuación
            palabras = contenido.split()
            contador_palabras = Counter(palabras)
            mas_comunes = contador_palabras.most_common(n)
            return mas_comunes
    except FileNotFoundError:
        print(f'el archivo {file_path2} no existe')
        return 0

# ejemplo de uso
print(palablasMasComunes(file_path2, 5))


