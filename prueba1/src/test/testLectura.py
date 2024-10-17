
'''PRACTICA 1 FP'''

import string
import os 

file_path = os.path.join(os.path.dirname(__file__), '..', 'lecturas', 'lin_quijote.txt')
file_path2 = os.path.join(os.path.dirname(__file__), '..', 'lecturas', 'archivo_palabras.txt')
file_path3 = os.path.join(os.path.dirname(__file__), '..', 'lecturas', 'palabras_random.csv')
file_path4 = os.path.join(os.path.dirname(__file__), '..', 'lecturas', 'vacio.csv')
file_path = os.path.normpath(file_path)


# ejercicio 6

def contar_palabra(file_path: str, cad: str, separador: str = ' ')-> int:
    try:
        with open(file_path, "r", encoding="utf-8") as fichero:
            contenido = fichero.read()
            contenido = contenido.lower()
            palabras = contenido.split() #dividir el contenido en palabras
            contador = palabras.count(cad) # contar las veces que aparece la palabra
            
            return contador
    except FileNotFoundError:
        print(f'el archivo {file_path} no existe')
        return 0


cad = "quijote"
separador = " "
resultado = contar_palabra(file_path, cad, separador)
print(f'la palabra {cad} se repite {resultado} veces')

print('................')
'--------------------------' 

# ejercicio 7

def buscar_lineas(file_path: str, cad: str)-> list:
    lineas_cadenas = []
    try: 
        with open(file_path, "r", encoding = "utf-8") as fichero:
            for linea in fichero: 
                if cad in linea: 
                    lineas_cadenas.append(linea.strip()) # buscamos la palabra tanto en mayuscula como en minuscula
                if cad.lower() in linea.lower():
                    lineas_cadenas.append(linea.strip())
            return lineas_cadenas
    except FileNotFoundError:
            print(f'el archivo {file_path} no existe')
            return []
        

cadena_a_buscar = "quijote"
lineas_encontradas = buscar_lineas(file_path, cad)

for linea in lineas_encontradas:
    print(f' la palabra {cadena_a_buscar} se encuentran en las siguiente linea: {linea}')
print('................')
'--------------------------'

# ejercicio 8


def encontrar_palabras(file_path2: str)-> list:
    try:
        with open(file_path2, "r", encoding="utf-8") as fichero:
            contenido = fichero.read()
            contenido = contenido.lower()
            contenido = contenido.translate(str.maketrans("", "", string.punctuation))
            palabras = contenido.split()
            palabras_unicas = set(palabras)
            
        return list(palabras_unicas)
    except FileNotFoundError:
        print(f'el archivo {file_path2} no existe')
        return []

palabras_unicas = encontrar_palabras(file_path2)

print(f'las palabras unicas encontradas son: {palabras_unicas}')
print('................')

'----------------------------'

# ejercicio 9

from typing import Optional

def longitud_promedio_lineas(file_path3: str)-> Optional[float]:
    try:
        with open(file_path3, "r", encoding="utf-8") as fichero:
            lineas = fichero.readlines()
            
            if not lineas:
                return None 
            total_longitud = 0
            numero_lineas = 0
            
            for linea in lineas:
                linea = linea.strip()
                longitud_linea = len(linea)
                total_longitud += longitud_linea
                numero_lineas += 1
                
            promedio = total_longitud / numero_lineas
            
            return promedio 
             
    except FileNotFoundError:
            print(f'el archivo {file_path3} no existe')
            return None

resultado = longitud_promedio_lineas(file_path3)
if resultado is not None:
    print(f'la longitud promedio de las lineas del primer archivo es: {resultado}')
else:
    print("el archivo no existe o esta vacio")
    
# buscamos en el segundo achivo "vacio.csv" 


resultado = longitud_promedio_lineas(file_path4)
if resultado is not None:
    print(f'la longitud promedio de las lineas del segundo archivo es: {resultado}')
else:
    print("el segundo archivo no existe o esta vacio")