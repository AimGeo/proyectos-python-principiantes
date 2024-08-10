'''
   # Consisten en pedirle al usuario que adivine
  un número elegido aleatoriamente por el programa.

   # El objetivo es que el usuario (quien dara el input) adivine correctamente el número
  (elegido aleatoriamente por el programa) en la menor cantidad de intentos posible.

   # El programa establece un rango de números posibles y
  elige aleatoriamente un número dentro de ese rango.

   # Luego, el programa le pide al usuario que adivine el número
  y le da una pista sobre si el número a adivinar es mayor o menor que el número
  que el usuario ha ingresado. De esta manera, el usuario puede ajustar sus conjeturas para acercarse al número correcto.

   # El juego continúa hasta que el usuario adivine el número correcto,
  momento en el que el programa le da una felicitación y le muestra
  el número de intentos que le tomó adivinar el número.
'''

import random

b= int(input("AIVINA EL NUMERO PAPU:  "))
a = random.randint(0,10)
intentos = 1

while a!= b:
    if a > b:
        intentos +=1
        print("el numero a adivinar es MAYOR")
        b=int(input("AIVINA EL NUMERO PAPU:  "))
        if a == b:
            print("Felicidades LO LOGRASTE ADIVINAR", "INTENTOS: ", intentos)
    if a < b:
        intentos +=1
        print("elnumero a adivinar es MENOR")
        b=int(input("AIVINA EL NUMERO PAPU:  "))
        if a == b:
            print("Felicidades LO LOGRASTE ADIVINAR", "INTENTOS: ", intentos)
