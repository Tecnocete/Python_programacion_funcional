'''
### 2.8. Ordenar una lista de cadenas por longitud.

### Descripción del ejercicio:

Crea una lista de cadenas y ordénala según su longitud, de menor a mayor usando una función lambda.

'''

strings = ["hello", "world", "python", "programming", "is", "fun"]
cadena_ordenada= sorted(strings, key=lambda x: len(x))

print(cadena_ordenada)
# Si se añade el argumento  reverse=True la ordena descendentemente
cadena_ordenada= sorted(strings, key=lambda x: len(x),reverse=True)
print(cadena_ordenada)

