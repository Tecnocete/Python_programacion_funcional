'''
### 2.2. Función `buscar_palabra`.

### Explicación del ejercicio:

Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
La función debe devolver una lista con todas las palabras de la lista original que contengan 
la palabra objetivo.
'''

def buscar_palabra(lista,palabra_buscada):
    lista_palabras= []
    for palabra in lista:
        if palabra_buscada in palabra:
            lista_palabras.append(palabra)
    return lista_palabras

lista_palabras_ejemplo = ["manzana", "banana", "naranja", "melocotón", "plátano"]
palabra_buscada_ejemplo = "na"

print (buscar_palabra(lista_palabras_ejemplo, palabra_buscada_ejemplo))