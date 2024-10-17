'''PRACTICAS FP'''

#ejercicio 1

def secuencia(n, k):
    producto = 1
    for i in range(k + 1):
        producto *=( n - i + 1)
    return producto 
'''valores'''
k = 2
n = 4
'''resultado'''
resultado = secuencia(n, k)
print(f'El producto de {n} y {k} es {resultado}')
        
#ejercicio 2

def secuencia_geo(a1, r, k):
    producto = 1
    for n in range(1, k + 1):
        an = a1*r**(n-1)
        producto *= an
    return producto
'''valores'''
a1 = 3 
r = 5 
k = 2
'''resultado'''
resultado = secuencia_geo(a1, r, k)
print(f'El resultado de a1= {a1}, r= {r} y k= {k} es {resultado}')

#ejercicio 3

import math 

def numero_comb(n, k):
    return math.factorial(n) //( math.factorial(k)*math.factorial(n-k))
'''valores'''
n = 4
K = 2
'''resultado'''
resultado = numero_comb(n, k)
print(f'el numero combinatorio de {n} y {k} es {resultado}')

#ejercicio 4

import math 

def binomial(n, k):
    return math.factorial(n) // (math.factorial(k)*math.factorial(n-k))

def ecuacion(n, k):
    suma = 0 
    for i in range(k):
        binomial_ecu = binomial(k+1, i+1)
        signo = (-1)**i
        producto = binomial_ecu * (k-i)**n
        suma += signo*producto
    return suma / math.factorial(k)
'''valores'''
n = 4
k = 2
resultado = ecuacion(n, k)
'''resultado'''
print(f'el resultado de la funcion siendo n= {n} y k= {k} es {resultado}')

#ejercicio 5

# definimos una funcion como 

def f(x):
    return 2*x**2 

def f_prime(x):
    return 4*x  

def metodo_newton(a, e, max_iter=100):
    x_n = a 
    for n in range(max_iter):
        fx_n = f(x_n)  
        if abs(fx_n) <= e:  
            return x_n  
        
        f_prime_x_n = f_prime(x_n)  
        
        if f_prime_x_n == 0:  
            raise ValueError("La derivada es cero")
        
       
        x_n = x_n - fx_n / f_prime_x_n
    
    raise ValueError("El método de Newton no converge en el número máx de iteraciones.")

a = 3.0  
e = 0.01  

try:
    resultado = metodo_newton(a, e)
    print(f'La solución encontrada es x0 = {resultado} tal que |f(x0)| <= {e}')
except ValueError as e:
    print(e)

    




        