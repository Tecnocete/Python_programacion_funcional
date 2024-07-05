'''
### 2.11. Mapear una lista.

### Descripción del ejercicio:

Crea una lista de números y utiliza una lambda junto con la función `map()` para elevar al cuadrado cada número en la lista.

'''

numbers = [1, 2, 3, 4, 5]

number_al_cuadrado = list(map(lambda x: x**2,numbers))

print (number_al_cuadrado)
