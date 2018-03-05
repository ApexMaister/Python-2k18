 #coding: utf­8


# Inicializaciones
salir = "N"

suma= 1

resultat=0

while ( salir=="N" ):
    # Hago cosas
    print suma ,"+"

    # Incremento

    resultat = resultat + suma
    suma = suma + 1



    # Activo indicador de salida si toca
    if ( resultat >= 15): # Condición de salid
        print "=",resultat
        salir = "S"
