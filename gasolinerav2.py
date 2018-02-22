#coding: utf8

# Arnau De Los Riscos

# Importacio de la llibreria os

import os

# Esborrem pantalla

os.system('clear')

# Menu

print """

    ############################
    #   Gasolineras Paquito    #
    ############################

    Buenos dias , Que le pongo??

    1 -Super Normal (1.5€)
    2 -Super Turbo (1.55€)
    3 -Sin plomo Normal (1.6€)
    4 -Sin plomo Con aditivos (sabor naranja) (1.65€)
    5 -Diesel Normal (1.7€)
    6 -Diesel Fast&Furius (1.75€)

 """

# Establiment de Variables

tipodegasolina= input ("Introduce El tipo de gasolina:   ")
print ""
litros = input ("Introduce Los Litros:   ")

# Condicions del Menu

if (litros !=0):
    if (tipodegasolina == 1):

        print""
        print "Su importe es de:  ",litros * 1.5 ,"€"
        print""

    elif (tipodegasolina == 2):

        print""
        print "Su importe es de:  ",litros * 1.55 ,"€"
        print""

    elif (tipodegasolina == 3):

        print""
        print "Su importe es de:  ",litros * 1.6 ,"€"
        print""

    elif (tipodegasolina == 4):

        print""
        print "Su importe es de:  ",litros * 1.65, "€"
        print""

    elif (tipodegasolina == 5):

        print""
        print "Su importe es de:  ",litros * 1.7 , "€"
        print""

    elif (tipodegasolina == 6):

        print""
        print "Su importe es de:  ",litros * 1.75 , "€"
        print""


# Control de Errors

    else:
        print""
        print "Opcion Incorrecta"
        print""

else:
        print""
        print "Numero de Litros Incorrecto"
        print""
