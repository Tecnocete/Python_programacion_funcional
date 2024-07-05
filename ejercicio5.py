'''
### 2.5. Función `combinar_listas`.

### Explicación del ejercicio:

Escribe una función que tome un número arbitrario de listas como argumentos y 
devuelva un diccionario donde las listas originales se combinan utilizando los índices como claves.

### Código a seguir:
'''

def combinar_listas (*args):
    lista_combinada = {}
    for indice, elementos in enumerate(zip(*args)):
        lista_combinada[indice] = list(elementos)
    return lista_combinada

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

resultado = combinar_listas(lista1, lista2, lista3)
print(resultado)