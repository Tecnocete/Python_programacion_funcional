'''
### 2.4. Función `factorial`.

###  Explicación del ejercicio:

- Se crea una función que calcula el factorial de un número utilizando recursividad.
- El factorial de un número entero no negativo, denotado como `n!`, es el producto de todos los enteros 
positivos menores o iguales a `n`. 
En otras palabras, el factorial de `n` se calcula multiplicando todos los números naturales desde 1 hasta `n`. 
'''

def factorial(n):
    if n == 0: 
        return 1 
    elif n <0:
        return ('no se puede hacer un factorial de números no naturales')
    else:
        return n*factorial(n-1)


print(factorial(14))