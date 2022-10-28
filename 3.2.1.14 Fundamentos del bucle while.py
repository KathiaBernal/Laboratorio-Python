"""
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

La figura ilustra la regla utilizada por los constructores:
altura: 3
bloques: 6

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.
Datos de Prueba

Entrada de muestra: 6
Salida esperada: La altura de la pirámide es: 3

Entrada de muestra: 20
Salida esperada: La altura de la pirámide es: 5

Entrada de muestra: 1000
Salida esperada: La altura de la pirámide es: 44

Entrada de muestra: 2
Salida esperada: La altura de la pirámide es: 1
"""

blocks = int(input("Ingresa el número de bloques: ")) #Ejemplo: 20

# Escribe tu código aquí.

height = 0
while blocks > height: # 20 > 0 || 19 > 1 || 17 > 2 || 14 > 3 || 10 > 4 || 5 no es mayor que 5, no es posible continuar el bucle.
    height += 1 # ALTURA AUMENTA 1 EN CADA BUCLE: 0 + 1 = 1 || 1 + 1 = 2 || 2 + 1 = 3 || 3 + 1 = 4 || 4 + 1 = 5 
    blocks -= height # LOS BLOQUES VAN DISMINUYENDO CONFORME AUMENTA LA ALTURA: 20 - 1 = 19 - 2 = 17 - 3 = 14 - 4 = 10 - 5 = 5
print("La altura de la pirámide:", height) # 1 || 2 || 3 || 4 || 5 || EN TOTAL SON CINCO CAPAS 