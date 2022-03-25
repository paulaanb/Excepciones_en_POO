#Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

#Importamos las librerias que necesitamos
import os
import sys
import Sentry
import smtplib




#Empezamos con el código principal
mail_server = smtplib.SMTP("localhost")

while True:
    try:
        correo = input("\nPor favor, introduzca la direccion de correo para poder acceder al sitio web deseado: "))
        print("\nEl correo introducido es : " ,correo)
        break
    except NameError:
        print("\nHa introducido una direccion de correo que no es valido.")
    except KeyboardInterrupt:
        print("\nHa cancelado la ejecución")
        break
#Debemos utilizar esto
try: 
    Operación normal
   ......................
except:
    Se produjo una excepción, ejecute este código
   ......................
else:
    Si no hay una ejecución anormal de este código