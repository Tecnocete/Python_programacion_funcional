'''
### Descripción del ejercicio:

Crea un diccionario que contenga nombres como claves y edades como valores, y luego ordénalo según la edad.

'''

people = {"Alice": 30, "Bob": 25, "Charlie": 35, "David": 40}

people_ordenado = dict(sorted(people.items(), key= lambda x: x[1]))
print (people_ordenado)

