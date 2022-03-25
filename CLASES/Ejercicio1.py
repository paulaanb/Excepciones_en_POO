#Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

#Importamos las librerias que necesitamos
import os
import sys
import Sentry
import smtplib
import re



#Empezamos con el código principal

while True:
    try:
        correo = "escribeaquitucorreo@mail.me"
        if "@" in correo:
	        print("El correo introducido es válido.")
        else:
	        print("El correo introducido no es válido.")
        
        print("\nEl correo introducido es : " ,correo)
        break
    except NameError:
        print("\nHa introducido una direccion de correo que no es valido.")
    except KeyboardInterrupt:
        print("\nHa cancelado la ejecución")
        break

#Definimos los comandos que se admiten en el correo para que sea valido
def correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

# Ejemplos de correos
correos = [
    "hola@", "ruben@profe.me", "soypaula@gmail.com",
    "ejercicio@excepciones.com", "correo@hotmail.com", "poo@gmail.com", "fallo",
    "no@se@hacerlo.com"
]

for correo in correos:
    print("Vamos a comprobar si el correo introducido '{}' es válido...{}".format(correo, correo_valido(correo)))