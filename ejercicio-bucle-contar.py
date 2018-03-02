#coding:utf-8

## Inicializaciones
salir = "N"
contador=1

while ( salir=="N" ):
    # Hago cosas
    print contador

    # Incremento
    contador = contador + 1
    # Activo indicador de salida si toca
    if ( contador >50): # Condición de salida
            salir = "S"
