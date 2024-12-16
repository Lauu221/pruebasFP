
''' PRACTICAS 1 FP '''


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.funciones.funcionesAct import producto_sec
from src.funciones.funcionesAct import secuencia_geo
from src.funciones.funcionesAct import numero_comb
from src.funciones.funcionesAct import ecuacion
from src.funciones.funcionesAct import metodo_newton


''' ejercicio 1 '''

print('ejercicio 1:')
n = 4
k = 2
resultado = producto_sec(n, k)
print(f'El producto de {n} y {k} es {resultado}')

print('................')

''' ejercicio 2 '''

print('ejercicio 2:')
a1 = 3 
r = 5 
k = 2
'''resultado'''
resultado = secuencia_geo(a1, r, k)
print(f'El resultado de a1= {a1}, r= {r} y k= {k} es {resultado}')


print('................')

''' ejercicio 3 '''

print('ejercicio 3:')
n = 4
k = 2
'''resultado'''
resultado = numero_comb(n, k)
print(f'el numero combinatorio de {n} y {k} es {resultado}')

print('................')

'''ejercicio 4'''

print('ejercicio 4:')
n = 4
k = 2
resultado = ecuacion(n, k)
'''resultado'''
print(f'el resultado de la funcion siendo n= {n} y k= {k} es {resultado}')


print('................')

''' ejercicio 5 '''

print('ejercicio 5:')
a = 3.0  
e = 0.01  

try:
    resultado = metodo_newton(a, e)
    print(f'La solución encontrada es x0 = {resultado} tal que |f(x0)| <= {e}')
except ValueError as e:
    print(e)
