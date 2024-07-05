'''
 ### 2.1. Función `frecuencia_letras`.

 ###  Explicación del ejercicio:

 Escribe una función que reciba una cadena de texto como parámetro
 y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
'''

def contador_letras (cadena):
    contador=dict()
    for letra in cadena.lower():
        
        if letra.isalpha():
            contador[letra]= contador.get(letra,0) + 1
    return contador

    

print (contador_letras("El patio de mi casa es particular, cuando llueve se moja como los demás"))