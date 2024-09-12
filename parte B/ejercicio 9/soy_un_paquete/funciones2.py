
def calcular_salario(cantidad_horas_trabajadas: int, antiguedad: int)-> int:
    aumento_antiguedad = antiguedad * 1.03
    salario = cantidad_horas_trabajadas * 10 + aumento_antiguedad
    return salario

def calcular_productividad(artefactos_producidos: int, cantidad_horas_trabajo: int)->float:
    productividad = artefactos_producidos / cantidad_horas_trabajo
    return productividad

def reportar_informacion_empleado():

    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    cantidad_horas_trabajadas = int(input("ingrese la cantidad de horas trabajadas: "))
    antiguedad = int(input("ingrese la cantidad de años de antiguedad: "))
    artefactos_producidos = int(input("ingrese la cantidad de artefactos producidos: "))
    cantidad_horas_trabajo = int(input("ingrese la cantidad de horas de trabajo: "))

    salario = calcular_salario(cantidad_horas_trabajadas, antiguedad)
    productividad = calcular_productividad(artefactos_producidos, cantidad_horas_trabajo)

    print("Reporte del Empleado:")
    print(f"nombre: {nombre}")
    print(f"edad: {edad} años")
    print(f"horas trabajadas: {cantidad_horas_trabajadas}")
    print(f"antigüedad: {antiguedad} años")
    print(f"salario: ${salario}")
    print(f"artefactos producidos: {artefactos_producidos}")
    print(f"productividad: {productividad} artefactos por hora")