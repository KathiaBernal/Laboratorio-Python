"""
scenario
Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

3x3 - 2x2 + 3x - 1

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo flotante.

Entrada de Muestra
x = 0
x = 1
x = -1

Salida Esperada
y = -1.0
y = 3.0
y = -9.0

"""

#x =  # codifica aquí tus datos de prueba
#x = float(x)
# escribe tu código aquí
#print("y =", y)

x = ((3*0**3)-(2*0**2)+(3*0)-1)
x = float(x)
y = x
print("y =", y)

x = ((3*1**3)-(2*1**2)+(3*1)-1)
x = float(x)
y = x
print("y =", y)

x = ((3*(-1)**3)-(2*(-1)**2)+(3*(-1))-1)
x = float(x)
y = x
print("y =", y)