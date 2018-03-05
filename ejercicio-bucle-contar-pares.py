# coding: utf­8


# Inicializaciones
salir = "N"
numero= 1
limite = input ("Introduce un numero Limite:")

while ( salir=="N" ):
    # Hago cosas
    if numero % 2 == 0:
        print numero
    

    # Incremento
    numero = numero + 1

    # Activo indicador de salida si toca
    if ( numero >= limite ): # Condición de salida
        salir = "S"
