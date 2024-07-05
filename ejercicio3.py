'''
### 2.3. Función `calcular_promedio`.

### Explicación del ejercicio:

Escribe una función que tome una lista de números como parámetro y un valor opcional `nota_aprobado`,
que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor 
o igual que `nota_aprobado`. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
La función debe devolver una tupla que contenga la media y el estado.

'''

def calcular_promedio(lista_notas, nota_aprobado = 5):
    resultado = 0
    for i in lista_notas:
        resultado += i
    nota_media= resultado/len(lista_notas)
    if nota_media<nota_aprobado:
        return (nota_media,'suspenso')
    else:
        return (nota_media, 'aprobado')
notas_alumnos = [6, 7, 8, 4, 5]

print (calcular_promedio(notas_alumnos))
    