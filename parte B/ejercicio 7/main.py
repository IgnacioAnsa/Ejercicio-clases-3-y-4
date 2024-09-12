# # Ejercicio 7:
# # Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
# # productos con impuestos para una determinada empresa:
# # La respuesta de chatgpt es:
# # def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
# # = 15):
# # resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
# # resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
# # resultado_final = resultado_nacional + resultado_exportaciones
# return resultado_final
# ¿Considera que cumple con los objetivos de una función?
# Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
# documente y denomine correctamente.

#Si, cumple con los objetivos de una funcion. Pero la declaracion de la misma, es decir, su nombre, hace referencia
# a una funcionalidad muy ambigua que abarca muchos calculos con muchos resultados, es mas preciso detallar y puntualizar en cada uno
# para facilitar separacion y la cohesion del codigo

from funciones1 import *
# llamo todas las funciones y les añado el argumento correspondiente

valor_ventas_nacionales, valor_exportaciones = ingresar_ventas()
calcular_iva(valor_ventas_nacionales)
calcular_retenciones(valor_exportaciones)
calcular_resultado_nacional(valor_ventas_nacionales)
calcular_resultado_exportaciones(valor_exportaciones)
calcular_resultado_final(valor_ventas_nacionales, valor_exportaciones)
