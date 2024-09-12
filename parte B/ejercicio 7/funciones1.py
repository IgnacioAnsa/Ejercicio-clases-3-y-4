# declaro funciones para ingresar las ventas, calcular el iva, las retenciones y los resultados, tanto nacional, exportaciones y el final

def ingresar_ventas()-> tuple:
    
    valor_ventas_nacionales = int(input("ingrese el valor de las ventas nacionales: "))
    valor_exportaciones = int(input("ingrese el valor de las exportaciones: "))
    return valor_ventas_nacionales, valor_exportaciones

def calcular_iva(valor_ventas_nacionales: int)->float:
    return valor_ventas_nacionales * 1.21
    
def calcular_retenciones(valor_exportaciones: int)->float:
    return valor_exportaciones * 1.15

def calcular_resultado_nacional(valor_ventas_nacionales: int)->float:
    resultado_nacional = calcular_iva(valor_ventas_nacionales)
    return resultado_nacional

def calcular_resultado_exportaciones(valor_exportaciones: int)->float:
    resultado_exportaciones = calcular_retenciones(valor_exportaciones)
    return resultado_exportaciones
    
def calcular_resultado_final(valor_ventas_nacionales: int, valor_exportaciones: int)->float:
    resultado_nacional = calcular_resultado_nacional(valor_ventas_nacionales)
    resultado_exportaciones = calcular_resultado_exportaciones(valor_exportaciones)
    resultado_final = resultado_nacional + resultado_exportaciones
    print(f"el resultado final es: {resultado_final}") 
    return resultado_final

