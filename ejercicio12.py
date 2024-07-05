'''
### 2.12. Contar elementos que cumplen una condición.

### Descripción del ejercicio:

Crea una lista de números y utiliza una lambda junto con la función `filter()` para filtrar los números mayores que 5. Luego, utiliza la función `len()` para contar cuántos números cumplen esta condición.

'''

numbers = [1, 2, 6, 7, 8, 3, 9, 10, 13]

number_filtrado= len(list(filter(lambda x: x>5,numbers)))

print (number_filtrado)

