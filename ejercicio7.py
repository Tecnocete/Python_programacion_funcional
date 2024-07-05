''''### 2.7. Función `procesar_datos`.

### Explicación del ejercicio:

Crea una función llamada `procesar_datos` que procesa una serie de datos dependiendo del tipo de operación especificada.'''

def procesar_datos (operacion,*args,**kwargs):
    if operacion == 'sumar':
        sumatorio = kwargs.get('valor inicial',0)
        for dato in args:
            sumatorio += dato
        return sumatorio
    elif operacion == 'restar':
        total= args[0]
        for dato in args[1:]:
            total-=dato
        return total
    elif operacion == 'multiplicar':
        factor = kwargs.get('factor',1) 
        for dato in args:
            factor*=dato
        return factor
    elif operacion == 'dividir':
        resultado= args[0]
        for dato in args[1:]:
            resultado/=dato
        return resultado
    else:
        raise ValueError (f"La operación: {operacion} no es válida.")
    
resultado_suma = procesar_datos('sumar', 1, 2, 3, 4, valor_inicial=10)


resultado_resta = procesar_datos('restar', 20, 5, 3)


resultado_multiplicacion = procesar_datos('multiplicar', 2, 3, 4, factor=2)


resultado_division = procesar_datos('dividir', 100, 5, 2)

    
