'''PRACTICAS FP'''

'''ejercicio 1'''

def producto_sec(n, k):
    producto = 1
    for i in range(k + 1):
        producto *=( n - i + 1)
    return producto 

        
'''ejercicio 2'''

def secuencia_geo(a1, r, k):
    producto = 1
    for n in range(1, k + 1):
        an = a1*r**(n-1)
        producto *= an
    return producto


'''ejercicio 3'''

import math 

def numero_comb(n, k):
    return math.factorial(n) //( math.factorial(k)*math.factorial(n-k))


'''ejercicio 4'''

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


'''ejercicio 5'''

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


    

        