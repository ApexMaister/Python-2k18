#coding: utf­8
import os
os.system ("clear")

# Inicializaciones
salir = "N"

suma= 1

resultat=0

while ( salir=="N" ):
   # Hago cosas


# Incremento
    if (suma % 2 == 0):
        print suma ,"+"
        resultat = resultat + suma

    suma = suma + 1



   # Activo indicador de salida si toca
    if ( resultat >=40):

# Condición de salida
        print "=",resultat
        salir = "S"
