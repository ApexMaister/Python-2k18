#coding:utf-8

## Inicializaciones
salir = "N"
contador=0

limite=input("Introduce el numero limite:  ")

while ( salir=="N" ):
    # Hago cosas
    print contador

    # Incremento
    contador = contador + 1
    # Activo indicador de salida si toca
    if ( contador == limite ): # Condición de salida
        print contador
        salir = "S"
