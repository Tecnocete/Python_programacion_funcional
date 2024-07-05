'''
### 2.6. Función `area_figura`

### Explicación del ejercicio:

Crea una función que calcule el área de una figura geométrica según el tipo especificado.

'''

def area_figura (**kwargs):
    if 'base' in kwargs and 'altura' in kwargs:
        base = kwargs['base']
        altura = kwargs['altura']
        area= base*altura/2
    elif 'radio' in kwargs:
        radio = kwargs['radio']
        area = 3.14 * radio**2
    elif 'lado' in kwargs:
        lado = kwargs['lado']
        area = lado**2
    else: 
        raise ValueError ('Tipo de firgura no soportada')
    
    return area
    

area_triangulo = area_figura(base=3, altura=4)

area_circulo = area_figura(radio=2)

area_cuadrado = area_figura(lado=5)

print (area_triangulo)
print (area_cuadrado)
print (area_circulo)        