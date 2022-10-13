"""
Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

Millas a kilómetros.
Kilómetros a millas.
No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.


Pon mucha atención a lo que esta ocurriendo dentro de la función print(). Analiza como es que se proveen múltiples argumentos para la función, y como es que se muestra el resultado.

Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo "millas son", y otros son variables (por ejemplo miles).

Resultado Esperado
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
"""

#kilometers = 12.25
#miles = 7.38

#miles_to_kilometers = ###
#kilometers_to_miles = ###

#print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
#print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = 7.38 * 1.61
kilometers_to_miles = 12.25/1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
