'''
### 2.9. Filtrar elementos de una lista de manera personalizada.

### Descripción del ejercicio:

Crea una lista de números y filtra los que son múltiplos de 3 y mayores que 10 utilizando una expresión de lista
y una condición personalizada.

### Pasos a seguir:
'''
numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

filtro_aplicado= [x for x in numbers if x>10 and x%3 ==0]

print (filtro_aplicado)